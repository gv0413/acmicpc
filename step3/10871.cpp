#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>

using std::pair;
using std::vector;
using pii=pair<int,int>;
using lint=long long;
int n;
int x;
int a[10001];
void input(){
	scanf("%d %d", &n, &x);
  for(int i=0; i<=n; i++){
    scanf("%d", &a[i]);
  }
}

void init(){

}
void process(){
  for(int i=0; i<n; i++){
    if(a[i] <x){
      printf("%d ", a[i]);
    }
  }
}

void output(){

}

int main(void){
	input();
	init();
	process();
	output();
	return 0;
}