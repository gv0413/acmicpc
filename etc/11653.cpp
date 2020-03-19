#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>

using std::pair;
using pii=pair<int,int>;
using lint=long long;

int n;
bool prime[10000001];
void input(){
	scanf("%d", &n);
}

void init(){
  memset(prime, 1, sizeof(prime));
}

void isPrime(){
  for(int i=2; i<10001; i++){
    if(prime[i]){
      for(int j=i*2; j<10000001; j+=i){
        prime[j] = false;
      }
    }
  }
}

void process(){
  for(int i=2; i<=n; i++){
    while (prime[i] && n%i==0){
      printf("%d\n", i);
      n /= i;
    }
    if(n==1) break;
  }
}

int main(void){
	input();
	init();
  isPrime();
	process();
	return 0;
}