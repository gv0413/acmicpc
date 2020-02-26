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
void input(){
	scanf("%d", &n);
}

void init(){

}
void process(){
	for(int i=1; i<=n; i++) {
    for(int j=1; j<=n-i; j++){
      printf(" ");
    }
    for(int k=1; k<=i; k++){
      printf("*");
    }
    printf("\n");
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