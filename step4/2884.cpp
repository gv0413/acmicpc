#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>

using std::pair;
using std::vector;
using pii=pair<int,int>;
using lint=long long;
int h, m;
void input(){
	scanf("%d %d", &h, &m);
}

void init(){

}

void process(){
  m = m - 45;
  if(m<0) {
    h = h-1;
    m = 60 + m;
    if(h<0){
      h = h + 24;
    }
  }
  printf("%d %d", h, m);
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