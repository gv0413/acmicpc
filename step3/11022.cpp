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
int num1, num2;
void input(){
	scanf("%d", &n);
}

void init(){

}

void process(){
	for(int i=0; i<n; i++) {
		scanf("%d %d", &num1, &num2);
		printf("Case #%d: %d + %d = %d\n", i+1, num1, num2, num1+num2);
	}
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