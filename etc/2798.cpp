#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>

using std::pair;
using std::vector;
using pii=pair<int,int>;
using lint=long long;

int n, m;
void input(){
	scanf("%d %d", &n, &m);
}

void init(){

}

void process(){
  int arr[n];
  int result = 0;
  for(int i=0; i<=n; i++){
    scanf("%d", &arr[i]);
  }
  for(int i=0; i<n-2; i++){
    for(int j=i+1; j<n-1; j++){
      for(int k=j+1; k<n; k++){
        if(arr[i]+arr[j]+arr[k]<=m && m - (arr[i]+arr[j]+arr[k]) < m - result){
          result = arr[i]+arr[j]+arr[k];
        }
      }
    }
  }
  printf("%d", result);
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