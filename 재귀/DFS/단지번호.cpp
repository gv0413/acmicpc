#include<cstdio>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#define MAX_N 25
int n;
int g[MAX_N][MAX_N];
int ch[MAX_N][MAX_N];
int cnt[MAX_N * MAX_N];

void input() {
  scanf("%d", &n);
  for(int i=0; i<n; i++) {
    for(int j=0; j<n+1; j++) {
      int tmp;
      scanf("%1d", &tmp);
      g[i][j] = tmp;
    }
  }
}

void DFS(u,v,cntIdx) {
  if (ch[u][v]) return;
  ch[u][v] = 1
  cnt[cntIdx] += 1

  if (u+1 < n && g[u+1][v] == 1 && !ch[u+1][v])
    DFS(u+1, v, cntIdx);

  if (u-1 >= 0 && g[u-1][v] == 1 && !ch[u-1][v])
    DFS(u-1, v, cntIdx);

  if (v-1 >= 0 && g[u][v-1] == 1 && !ch[u][v-1])
    DFS(u, v-1, cntIdx);

  if (v+1 < n && g[u][v+1] == 1 && !ch[u][v+1])
    DFS(u, v+1, cntIdx);
}

void process() {
  for i in range(n)
    for j in range(n) {
      if (ch [i][j] == 0 and g[i][j] == 1)
      cnt.append(0);
      cntIdx = len(cnt) - 1
      DFS(i, j, cntIdx)
    }
}

void output() {

}

int main(){
  input();
  process();
  output();
}