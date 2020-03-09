#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>

using std::pair;
using pii=pair<int,int>;
using lint=long long;

int n, res;
int arr[101];
void input(){
	scanf("%d", &n);
}

void init(){
  arr[0]=0;
  arr[1]=1;
}

void process(){
  for(int i=2; i<=n; i++){
    arr[i] = arr[i-1] + arr[i-2];
  }
  res = arr[n];
}

void output(){
  printf("%d", res);
}

int main(void){
	input();
	init();
	process();
	output();
	return 0;
}