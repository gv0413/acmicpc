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
  int arr[1000001];
  for(int i=0; i<n; i++){
    scanf("%d", &arr[i]);
  }

  sort(arr, arr+n);
  printf("%d %d", arr[0], arr[n-1]);
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