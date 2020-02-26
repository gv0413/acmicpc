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
bool arr[10001];

int dn(int n){
  return n + (n/1000) + (n%1000)/100 + (n%100)/10 + n%10;
}

void init(){
	for(int i=0; i<10001; i++){
		int ans = dn(i);
		if(ans<10001){
			arr[ans] = true;
		}
	}	

	for(int i=0; i<10001; i++){
		if(!arr[i]){
			printf("%d\n", i);
		}
	}
} 

void process(){
  
}

void output(){
}

int main(void){
	init();
	process();
	output();
	return 0;
}