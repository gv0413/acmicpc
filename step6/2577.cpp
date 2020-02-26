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

int a, b, c;
int arr[10] = {0};
void input(){
	scanf("%d %d %d", &a, &b, &c);
}
void init(){
  int result = a*b*c;
  int idx;
  while(result){
    idx = result % 10;
    arr[idx] = arr[idx]+1;
    result = result/10;
  }
  for(int i=0; i<10; i++){
    printf("%d\n", arr[i]);
  }
}

void process(){
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