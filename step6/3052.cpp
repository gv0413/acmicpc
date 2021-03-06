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

int mod[10] = {0};
void input(){
  for(int i=0; i<10; i++){
    scanf("%d", &mod[i]);
  }
}

void init(){
	int cnt=0;
  int arr[42] = {0};
  for(int i=0; i<10; i++){
    mod[i] = mod[i] % 42;
  }


  for (int i=0; i<10; i++){
    arr[mod[i]]++;
  }

  for(int i=0; i<42; i++){
    if(arr[i]!=0){
      cnt++;
    }
  }
  printf("%d", cnt);
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