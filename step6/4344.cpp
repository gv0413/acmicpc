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

int C, N;
int arr [1001];
void input(){
  scanf("%d", &C);
  for(int j=0; j<C; j++){
    int sum=0;
    double avg=0;
    int cnt=0;
    scanf("%d", &N);
    for(int i=0; i<N; i++){
      scanf("%d", &arr[i]);
      sum = sum + arr[i]; 
    }
    avg = sum/N; 
    for(int i=0; i<N; i++){
      if(arr[i]>avg){
        cnt++;
      }
    }
    printf("%.3f%%\n", (float)cnt/N*100);
  }

  
}

void init(){
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