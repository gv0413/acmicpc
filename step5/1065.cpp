#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;
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
  int a,b,c;
  int cnt = 0;
  for(int i=1; i<=n; i++){
    a = i/100;
    b = (i%100)/10;
    c = i%10;
    if(a==0){
      cnt++;
    }
    else{
      int d = a - b;
      if(b-c == d){
        cnt++;
      }
    }
  }
  printf("%d", cnt);
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