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
int x;
void input(){
	scanf("%d %d %d", &a, &b, &c);
}

void init(){

}

void process(){
  int arr[3] = {a, b, c};
  sort(arr, arr+3);
  printf("%d", arr[1]);
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