#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>

using std::pair;
using pii=pair<int,int>;
using lint=long long;

int n, m;
int max = 9;
int arr[9];
bool visited[9];
void input(){
	scanf("%d %d", &n, &m);
}

void init(){
  memset(visited, 0, sizeof(visited));
}

void process(int cur){
  if(cur == m){
    for(int i=0; i<m; i++){
      printf("%d ", arr[i]);
    }
    printf("\n");
    return;
  }

  for(int i=1; i<=n; i++){
    if(!visited[i]){
      visited[i] = true;
      arr[cur] = i;
      process(cur + 1);
      visited[i] = false;
    }
  }
}

void output(){
}

int main(){
	input();
	init();
	process(0);
	output();
	return 0;
}