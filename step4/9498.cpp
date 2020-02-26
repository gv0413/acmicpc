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
void input(){
	scanf("%d", &n);
}

void init(){

}

void process(){
  if(n>=90 && n<=100) printf("A");
  else if(n>=80 && n<=89) printf("B");
  else if(n>=70 && n<=79) printf("C");
  else if(n>=60 && n<=69) printf("D");
  else printf("F");
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