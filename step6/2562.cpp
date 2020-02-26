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

int arr[9];
void input(){
	for(int i=0; i<9; i++){
    scanf("%d", &arr[i]);
  }
}
void init(){
  int max = arr[0];
  int idx = 1;
  for(int i=0; i<9; i++){
    if(max < arr[i]){
      max = arr[i];
      idx = i+1;
    }
  }
  printf("%d\n%d", max, idx);
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