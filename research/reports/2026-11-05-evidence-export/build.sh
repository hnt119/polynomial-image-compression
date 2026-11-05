#!/bin/sh
set -eu
cd "$(dirname "$0")"
source_dir=$(pwd)
build_dir=$(mktemp -d -t polynomial-evidence.XXXXXX)
trap 'printf "Build diagnostics retained in %s\n" "$build_dir" >&2' 0
cp *.tex references.bib "$build_dir/"
cp -R figures "$build_dir/"
cd "$build_dir"
export TZ=UTC SOURCE_DATE_EPOCH=1793836800 FORCE_SOURCE_DATE=1
latex_pass() { pdflatex -interaction=nonstopmode -halt-on-error -file-line-error "$1.tex" > "$1.stdout" || { cat "$1.stdout" >&2; exit 1; }; }
latex_pass report
bibtex report > bibliography.stdout || { cat bibliography.stdout >&2; exit 1; }
latex_pass report
latex_pass report
latex_pass summary
latex_pass summary
if grep -E 'Overfull|LaTeX Warning|Package .* Warning|Missing character|Undefined control' report.log summary.log; then
  printf '%s\n' 'Review these typesetting diagnostics before releasing the PDFs.' >&2
  exit 1
fi
cp report.pdf summary.pdf "$source_dir/"
cd "$source_dir"
rm -rf "$build_dir"
trap - 0
