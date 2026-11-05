#!/usr/bin/env python3
"""Build the two reports from Markdown, offline. Requires python-docx, lxml,
reportlab, pdftoppm and either a complete local Tectonic cache or XeLaTeX.
No dependencies are downloaded. See the adjacent README for the build command.
"""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.shared import Inches, Pt, RGBColor
from reportlab.lib.colors import HexColor
from reportlab.pdfgen.canvas import Canvas

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EPOCH = int(dt.datetime(2026, 11, 5, tzinfo=dt.timezone.utc).timestamp())
LINK = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
MATH = re.compile(r'(\$[^$]+\$|\*\*[^*]+\*\*|\*[^*]+\*)')
NAVY, TEAL, GRAY, PALE = '#172C38', '#146464', '#4E6370', '#E8F0F0'

def source_name(href):
    if href.startswith('https://'):
        return href
    return (HERE / href).resolve().relative_to(ROOT).as_posix()

def bib_entries():
    data = (HERE / 'references.bib').read_text()
    items = []
    for key, body in re.findall(r'@misc\{(\w+),\s*(.*?)\n\}', data, re.S):
        fields = dict(re.findall(r'(\w+)\s*=\s*\{(.*?)\}', body, re.S))
        items.append((key, fields))
    return items

def blocks(path):
    """A deliberate small Markdown subset. Links in Sources lines are locators."""
    lines = path.read_text().splitlines(); result=[]; i=0
    while i < len(lines):
        v=lines[i].strip();i+=1
        if not v: continue
        if v == '<!-- page -->': result.append(('page',''))
        elif v.startswith('### '): result.append(('sub',v[4:]))
        elif v.startswith('## '): result.append(('section',v[3:]))
        elif v.startswith('# '): result.append(('title',v[2:]))
        elif v.startswith('Sources: '): result.append(('sources',LINK.findall(v)))
        elif v.startswith('!['): result.append(('figure',LINK.findall(v[1:])[0]))
        elif v=='$$':
            start=i
            while i<len(lines) and lines[i].strip()!='$$': i+=1
            if i==len(lines): raise ValueError('Unclosed display in '+str(path))
            result.append(('display',' '.join(lines[start:i])));i+=1
        elif '·' in v and len(result)==1: result.append(('deck',v))
        else: result.append(('body',v))
    return result

def esc(s):
    return ''.join({'&':r'\&','#':r'\#','%':r'\%','_':r'\_',
                    '{':r'\{','}':r'\}','–':'--','—':'---','·':r'\textperiodcentered{}'}.get(x,x) for x in s)

def tex_inline(s):
    r=[]
    for token in MATH.split(s):
        if token.startswith('$') and token.endswith('$'): r.append(token)
        elif token.startswith('**'): r.append(r'\textbf{'+tex_inline(token[2:-2])+'}')
        elif token.startswith('*'): r.append(r'\textit{'+tex_inline(token[1:-1])+'}')
        else: r.append(esc(token))
    return ''.join(r)

def slug(s): return re.sub('[^a-z0-9]+','-',s.lower()).strip('-')

PREAMBLE = r"""% Generated from the adjacent canonical Markdown with build.py.
% Compile with XeLaTeX or Tectonic. No network access or fonts shipped.
\documentclass[12pt,a4paper]{article}
\usepackage{amsmath,amssymb}
\usepackage{newtxtext,newtxmath}
\DeclareMathSizes{9.1}{10}{7}{7}
\DeclareMathSizes{8.6}{10}{7}{7}
\usepackage[left=22mm,right=22mm,top=21mm,bottom=24mm]{geometry}
\usepackage{xurl}
\usepackage[hidelinks]{hyperref}
\urlstyle{same}
\hypersetup{pdfauthor={Polynomial Image Compression Project},pdfcreator={Offline evidence export}}
\setlength{\parindent}{0pt}
\setlength{\parskip}{7pt}
\setlength{\emergencystretch}{2em}
\raggedbottom
\newcommand{\teal}[1]{{\special{color push rgb .08 .38 .38}#1\special{color pop}}}
\newcommand{\kicker}[1]{{\small\teal{\textbf{#1}}\par}}
\newcommand{\headone}[1]{\vspace{6pt}{\raggedright\hyphenpenalty=10000\fontsize{22}{25}\selectfont\bfseries #1\par}\vspace{3pt}}
\newcommand{\headtwo}[1]{\vspace{3pt}{\large\bfseries #1\par}}
\newcommand{\sourceitem}[3]{\par{\fontsize{9.1}{11.3}\selectfont\textbf{#1}\quad\href{#2}{\nolinkurl{#3}}\par}}
\newcommand{\localfigure}[1]{\par\noindent\hbox to \linewidth{\hfil\XeTeXpicfile "#1" width .98\linewidth\hfil}\par}
\makeatletter
\def\ps@evidence{\def\@oddhead{}\let\@evenhead\@oddhead
\def\@oddfoot{\footnotesize Polynomial Image Compression\hfil 5 November 2026\quad/\quad\thepage}
\let\@evenfoot\@oddfoot}
\makeatother
\pagestyle{evidence}
\begin{document}
"""
def make_tex(name, b):
    bib=dict(bib_entries())
    keys={v['howpublished']:k for k,v in bib.items()}
    cites=[];out=[PREAMBLE];page=1;sec='start';eq=0
    for k,v in b:
        if k=='page':
            page+=1;out.append(r'\clearpage\kicker{'+('PROFESSOR BRIEF' if name=='professor_brief' else 'RESEARCH REPORT')+r'\quad / \quad '+str(page).zfill(2)+'}')
        elif k=='title':
            out += [r'\hypersetup{pdftitle={'+esc(v)+'}}',r'\kicker{MATHEMATICS \quad / \quad EVIDENCE SNAPSHOT}',r'{\raggedright\hyphenpenalty=10000\fontsize{27}{30}\selectfont\bfseries '+esc(v)+r'\par}']
        elif k=='deck':out.append(r'{\small '+esc(v)+r'\par}')
        elif k=='section':
            sec=slug(v);eq=0;out.append(r'\phantomsection\label{sec:'+sec+r'}\headone{'+esc(v)+'}')
        elif k=='sub':out.append(r'\headtwo{'+esc(v)+'}')
        elif k=='body':out.append(tex_inline(v)+r'\par')
        elif k=='display':
            eq+=1;out.append(r'\begin{equation*}\tag*{}\label{eq:'+sec+'-'+str(eq)+'}\n'+v+'\n'+r'\end{equation*}')
        elif k=='figure':out.append(r'\localfigure{'+v[1]+'}')
        elif k=='sources':
            rows=[r'\vspace{2pt}\kicker{PROOF AND EVIDENCE}']
            for label,href in v:
                rel=source_name(href)
                tag=keys.get(rel,'')
                extra=''
                if tag and name=='research_report':
                    if tag not in cites:cites.append(tag)
                    extra=r' \cite{'+tag+'}'
                rows.append(r'\sourceitem{'+esc(label)+extra+'}{'+href+'}{'+rel+'}')
            out.extend(rows)
    if name=='research_report':
        out.append(r'\clearpage\kicker{SOURCE GUIDE}\begingroup\small\setlength{\parskip}{1pt}\begin{thebibliography}{99}\setlength{\itemsep}{2pt}')
        for k in cites:
            v=bib[k];out.append(r'\bibitem{'+k+r'}\textbf{'+esc(v['title'])+r'}. '+esc(' '.join(filter(None,[v.get('author'),v.get('month'),v['year']])))+'. '+esc(v['note'])+r'.\par{\fontsize{8.6}{10}\selectfont\nolinkurl{'+v['howpublished']+r'}\par}')
        out.append(r'\end{thebibliography}\endgroup')
    out.append(r'\end{document}')
    (HERE/(name+'.tex')).write_text('\n\n'.join(out)+'\n')

# A small, strict TeX-math reader for the brief's native Word equations.
# Unknown commands fail the build instead of leaving TeX or pictures in Word.
SYMS={'le':'≤','ge':'≥','ne':'≠','in':'∈','subset':'⊂','omega':'ω','tau':'τ',
      'epsilon':'ε','gamma':'γ','nu':'ν','infty':'∞','cdot':'·','Theta':'Θ',
      'qquad':'    ','quad':'  ', ',':' ','log':'log','exp':'exp',
      'lvert':'|','rvert':'|','to':'→','ldots':'…','leq':'≤','geq':'≥'}
STYLE={'mathbb':{'E':'𝔼','R':'ℝ','Z':'ℤ','Q':'ℚ'},
       'mathcal':{'R':'ℛ','O':'𝒪','G':'𝒢','U':'𝒰'}}
def elem(s):
    return OxmlElement('m:'+s)
def mr(text):
    r=elem('r'); t=elem('t'); t.text=text
    t.set(qn('xml:space'),'preserve');r.append(t);return r
def wr(s, el):
    n=elem(s)
    for x in el:n.append(x)
    return n
def math_xml(source):
    tokens=re.findall(r'\\[A-Za-z]+|\\.|[^\s]',source)
    pos=0
    def arg():
        nonlocal pos
        if pos>=len(tokens):raise ValueError(source)
        if tokens[pos]=='{':
            pos+=1;vals=seq()
            if pos>=len(tokens) or tokens[pos]!='}':raise ValueError(source)
            pos+=1;return vals
        return atom()
    def atom():
        nonlocal pos
        tok=tokens[pos];pos+=1
        if tok=='{':
            pos-=1;return arg()
        if tok=='\\frac':
            n=elem('f');n.append(wr('num',arg()));n.append(wr('den',arg()));return [n]
        if tok=='\\sqrt':
            n=elem('rad');pr=elem('radPr');hide=elem('degHide');hide.set(qn('m:val'),'1');pr.append(hide);n.append(pr);n.append(elem('deg'));n.append(wr('e',arg()));return [n]
        if tok.startswith('\\'):
            c=tok[1:]
            if c in STYLE:
                val=''.join(t.text for n in arg() for t in n.iter(qn('m:t')))
                return [mr(STYLE[c][val])]
            if c not in SYMS:raise ValueError('Unrecognized Word math command '+tok+' in '+source)
            tok=SYMS[c]
        return [mr('−' if tok=='-' else tok)]
    def seq():
        nonlocal pos
        result=[]
        while pos<len(tokens) and tokens[pos]!='}':
            val=atom();sub=sup=None
            while pos<len(tokens) and tokens[pos] in ('_','^'):
                typ=tokens[pos];pos+=1
                if typ=='_':sub=arg()
                else:sup=arg()
            if sub is not None or sup is not None:
                el=elem('sSubSup' if sub is not None and sup is not None else ('sSub' if sub is not None else 'sSup'))
                el.append(wr('e',val))
                if sub is not None:el.append(wr('sub',sub))
                if sup is not None:el.append(wr('sup',sup))
                val=[el]
            result+=val
        return result
    nodes=seq()
    if pos!=len(tokens):raise ValueError('Unparsed math '+source)
    return wr('oMath',nodes)

def word_link(p,label,target):
    hl=OxmlElement('w:hyperlink');hl.set(qn('r:id'),p.part.relate_to(target,RT.HYPERLINK,is_external=True))
    r=OxmlElement('w:r');pr=OxmlElement('w:rPr');c=OxmlElement('w:color');c.set(qn('w:val'),'146464');pr.append(c)
    r.append(pr);t=OxmlElement('w:t');t.text=label;r.append(t);hl.append(r);p._p.append(hl)
def word_text(p,v):
    for tok in MATH.split(v):
        if tok.startswith('$') and tok.endswith('$'):p._p.append(math_xml(tok[1:-1]))
        elif tok.startswith('**'):p.add_run(tok[2:-2]).bold=True
        elif tok.startswith('*'):p.add_run(tok[1:-1]).italic=True
        else:p.add_run(tok)
def setstyle(s,size,space=4,face='Cambria',color='172C38',bold=False):
    s.font.name=face;s.font.size=Pt(size);s.font.bold=bold;s.font.color.rgb=RGBColor.from_string(color)
    pf=s.paragraph_format;pf.space_before=Pt(0);pf.space_after=Pt(space);pf.line_spacing=1.10
def word(b):
    d=Document();sec=d.sections[0];sec.page_width=Inches(8.27);sec.page_height=Inches(11.69)
    sec.left_margin=sec.right_margin=Inches(.86);sec.top_margin=Inches(.77);sec.bottom_margin=Inches(.79)
    prop=d.core_properties;prop.title=b[0][1];prop.author='Polynomial Image Compression Project';prop.last_modified_by='Polynomial Image Compression Project'
    prop.subject='Research evidence for a professor briefing';prop.keywords='quadratic forms; norm orbits; polynomial images'
    prop.created=prop.modified=dt.datetime(2026,11,5,0,0,0)
    for nm in ('Title','Subtitle','Heading 1','Heading 2'):
        st=d.styles[nm]; pPr=st._element.find(qn('w:pPr'))
        if pPr is not None:
            for border in pPr.findall(qn('w:pBdr')):pPr.remove(border)
    for nm,size,sp,ff,co,bold in [('Normal',11.5,7,'Cambria','172C38',False),('Title',28,5,'Cambria','000000',True),
       ('Heading 1',20,8,'Cambria','172C38',True),('Heading 2',14,5,'Cambria','172C38',True),('Subtitle',10,10,'Calibri','526571',False)]:
        setstyle(d.styles[nm],size,sp,ff,co,bold)
    for nm,size,col,sp in [('Locator',8.2,'4E6370',3),('Kicker',9,'146464',5)]:
        st=d.styles.add_style(nm,WD_STYLE_TYPE.PARAGRAPH);setstyle(st,size,sp,'Calibri',col,nm=='Kicker')
    page=1
    for k,v in b:
        if k=='page':
            page+=1;d.add_page_break();d.add_paragraph('PROFESSOR BRIEF     /     '+str(page).zfill(2),'Kicker')
        elif k=='title':d.add_paragraph('MATHEMATICS     /     EVIDENCE SNAPSHOT','Kicker');d.add_paragraph(v,'Title')
        elif k=='section':d.add_heading(v,1)
        elif k=='sub':d.add_heading(v,2)
        elif k=='deck':d.add_paragraph(v,'Subtitle')
        elif k=='body':word_text(d.add_paragraph(),v)
        elif k=='display':
            p=d.add_paragraph();p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.paragraph_format.space_after=Pt(8)
            p._p.append(math_xml(v))
        elif k=='figure':
            p=d.add_paragraph();p.alignment=WD_ALIGN_PARAGRAPH.CENTER
            sh=p.add_run().add_picture(str(HERE/v[1]),width=Inches(6.33));sh._inline.docPr.set('descr',v[0])
        elif k=='sources':
            d.add_paragraph('PROOF AND EVIDENCE','Kicker')
            for label,link in v:
                p=d.add_paragraph(style='Locator');p.add_run(label+'   ').bold=True;word_link(p,source_name(link),link)
    foot=sec.footer.paragraphs[0];foot.alignment=WD_ALIGN_PARAGRAPH.RIGHT
    foot.add_run('Polynomial Image Compression    /    5 November 2026    /    ').font.size=Pt(8)
    fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');foot._p.append(fld)
    dst=HERE/'professor_brief.docx'
    with tempfile.TemporaryDirectory() as td:
        raw=Path(td)/'raw.docx';d.save(raw)
        # The Word package is not signed. Normalize ZIP timestamps for rebuilds.
        with ZipFile(raw) as src,ZipFile(dst,'w',compression=ZIP_DEFLATED) as out:
            for n in sorted(src.namelist()):
                info=ZipInfo(n,(2026,11,5,0,0,0));info.compress_type=ZIP_DEFLATED
                out.writestr(info,src.read(n))

def render_figures(tmp):
    width=480
    def label(c,x,y,s,size=10,color=NAVY,b=False):
        c.setFont('Helvetica-Bold' if b else 'Helvetica',size);c.setFillColor(HexColor(color));c.drawString(x,y,s)
    def line(c,x1,y1,x2,y2):
        c.setStrokeColor(HexColor('#8AA3A4'));c.setLineWidth(1.4);c.line(x1,y1,x2,y2)
    def box(c,x,y,w,h,txt):
        c.setFillColor(HexColor(PALE));c.roundRect(x,y,w,h,4,fill=1,stroke=0);label(c,x+9,y+h/2-3,txt,10)
    figs=HERE/'figures';figs.mkdir(exist_ok=True)
    def finish(c,file):
        c.showPage();c.save()
        env=os.environ.copy();env.setdefault('XDG_CACHE_HOME',str(tmp/'font-cache'))
        subprocess.run(['pdftoppm','-singlefile','-r','180','-png',str(tmp/(file+'.pdf')),str(figs/file)],env=env,check=True)
    c=Canvas(str(tmp/'orbit-labels.pdf'),pagesize=(width,87),invariant=1)
    for x,title in [(8,'NONZERO PAIRS'),(172,'OCCUPIED LABELS'),(389,'OUTPUT')]:label(c,x,72,title,8,TEAL,True)
    for y in (48,20):
        for x in (10,23,36,49):
            c.setFillColor(HexColor(TEAL if y==48 else GRAY));c.circle(x,y,3.0,stroke=0,fill=1)
        line(c,61,y,165,y)
        box(c,172,y-9,127,19,('First ideal, norm q' if y==48 else 'Second ideal, norm q'))
        line(c,302,y,363,34)
    line(c,363,34,388,34);box(c,391,25,78,19,'Norm q')
    label(c,8,1,'Schematic only. Distinct order ideals may occur at the same norm.',8,GRAY)
    finish(c,'orbit-labels')
    records=json.loads((ROOT/'research/notes/2026-10-11-balanced-full-fibers/data.json').read_text())['cases']
    c=Canvas(str(tmp/'fiber-audit.pdf'),pagesize=(width,85),invariant=1)
    label(c,4,69,'SOURCES WITH EXACTLY FOUR FULL TARGETS',8,TEAL,True)
    for row,y in zip(records,[45,19]):
        m=row['pair_weighted_histogram']['4'];n=row['ordered_pairs'];f=m/n
        label(c,4,y,'Depth '+str(row['r']),9,NAVY,True);c.setFillColor(HexColor(PALE));c.rect(53,y,209,8,fill=1,stroke=0)
        c.setFillColor(HexColor(TEAL));c.rect(53,y,209*f,8,fill=1,stroke=0)
        label(c,276,y,f'{m:,} of {n:,}  ({100*f:.1f}%)',9)
    label(c,4,1,'Exact finite observations; percentages are rounded. Source: retained full-fiber audit.',8,GRAY)
    finish(c,'fiber-audit')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tectonic',default=os.environ.get('TECTONIC') or shutil.which('tectonic'))
    parser.add_argument('--cache-dir',default=os.environ.get('TECTONIC_CACHE_DIR'))
    parser.add_argument('--no-pdf',action='store_true',help='Emit native and TeX sources only')
    args=parser.parse_args()
    with tempfile.TemporaryDirectory() as dirname:
        tmp=Path(dirname);render_figures(tmp)
        for name in ['professor_brief','research_report']:
            b=blocks(HERE/(name+'.md'));make_tex(name,b)
            if name=='professor_brief':word(b)
            if args.no_pdf:continue
            env=os.environ.copy();env['SOURCE_DATE_EPOCH']=str(EPOCH)
            if args.cache_dir:env['TECTONIC_CACHE_DIR']=args.cache_dir
            if args.tectonic:
                cmd=[args.tectonic,'-X','compile','--only-cached','--keep-logs','--outdir',str(tmp),name+'.tex']
                subprocess.run(cmd,cwd=HERE,env=env,check=True)
            elif shutil.which('xelatex'):
                cmd=['xelatex','-interaction=nonstopmode','-halt-on-error','-no-shell-escape','-output-directory='+str(tmp),name+'.tex']
                for _ in range(2):subprocess.run(cmd,cwd=HERE,env=env,check=True)
            else:raise SystemExit('Need offline Tectonic with a populated cache or local XeLaTeX.')
            log=(tmp/(name+'.log')).read_text(errors='replace')
            if ('undefined references' in log or 'Missing character:' in log
                or re.search(r'Overfull \\[hv]box', log)):
                raise SystemExit('Unresolved reference, missing glyph, or overfull box in '+name+':\n'+'\n'.join(x for x in log.splitlines() if 'undefined' in x or 'Missing character' in x or 'Overfull' in x))
            shutil.copyfile(tmp/(name+'.pdf'),HERE/(name+'.pdf'))

if __name__=='__main__':main()
