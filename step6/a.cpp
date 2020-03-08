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
double arr[1001];
void input(){
  scanf("%d", &n);
  for(int i=0; i<n; i++){
    scanf("%lf", &arr[i]);
  }
}

void init(){
  double max = arr[0];
  double sum = 0;
  for(int i=0; i<n; i++){
    if(max < arr[i]){
      max = arr[i];
    }
  }

  for(int i=0; i<n; i++){
    arr[i] = (arr[i] / max) * 100;
  }
  
  for(int i=0; i<n; i++){
    sum = sum + arr[i];
  }
  printf("%.2f\n", sum/n);

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