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
  if(n%4==0 && n%100!=0 || n%400==0) printf("1");
  else printf("0");
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