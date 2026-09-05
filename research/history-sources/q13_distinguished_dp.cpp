#include <bits/stdc++.h>
using namespace std;
int main(){const int q=13,ALL=(1<<q)-1;int Q[q][q];for(int x=0;x<q;x++)for(int y=0;y<q;y++)Q[x][y]=(x*x+x*y+y*y)%q;
 int maxByM[14]{};int arg[14]{};vector<uint16_t>I(1<<q);vector<array<int,2>>dp(1<<q);
 for(int T=0;T<1<<q;T++)if(!(T&1)){int m=__builtin_popcount((unsigned)T);uint16_t N[q]{};for(int x=0;x<q;x++)for(int y=0;y<q;y++)if((x==0&&y==0)||(T>>Q[x][y]&1))N[x]|=1<<y;I[0]=ALL;for(int S=1;S<=ALL;S++){int b=__builtin_ctz((unsigned)S);I[S]=I[S^(1<<b)]&N[b];}
  for(auto &a:dp)a={-1000000,-1000000};dp[0][0]=0;
  for(int S=1;S<=ALL;S++){int add=__builtin_popcount((unsigned)I[S]);for(int U=S;U;U&=U-1){int x=__builtin_ctz((unsigned)U),P=S^(1<<x);for(int f=0;f<2;f++)if(dp[P][f]>-999999){int nf=f;if(x==0 && (I[S]&1))nf=1;dp[S][nf]=max(dp[S][nf],dp[P][f]+add);}}}
  int e=dp[ALL][1];if(e>maxByM[m])maxByM[m]=e,arg[m]=T;
 }
 for(int m=0;m<=12;m++){cout<<m<<" maxE="<<maxByM[m]<<" Dmin="<<13*m-maxByM[m]<<" T=";for(int t=1;t<q;t++)if(arg[m]>>t&1)cout<<t<<",";cout<<"\n";}
}
