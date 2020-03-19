#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <math.h>

using std::pair;
using std::vector;
using pii=pair<int,int>;
using lint=long long;

int n;
bool prime[1000001];
int arr[1000001];
vector<pii> v[101];
int input_exp[1000001];

void input(){
	scanf("%d", &n);
  for(int i=0; i<n; i++){
    scanf("%d", &arr[i]);
  }
}

void init(){
  memset(prime, 1, sizeof(prime));
  memset(input_exp, 0, sizeof(input_exp));
}

void isPrimeNum(){
  for(int i=2; i<1001; i++){
    if(prime[i]){
      for(int j=i*2; j<1000001; j+=i ){
        prime[j] = false;
      }
    }
  }
}


void factorization(){
  for(int i=0; i<n; i++){
    int k = 2;
    int k_cnt = 0 ;
    while(arr[i] != 1){
      if(arr[i] % k ==0 && prime[k]){
        if(k_cnt == 0){
          k_cnt++;
          v[i].push_back(std::make_pair(k,k_cnt));
          arr[i] /= k;
          input_exp[k]++;
        }
        else{
          k_cnt++;
          v[i].back().second = k_cnt;
          arr[i] /= k;
          input_exp[k]++;
        }
      }
      else {
        k++;
        k_cnt = 0 ;
      }
    }
  }
}


void output(){
  int score = 1;
  int cnt = 0;
  int gcd_exp = 0;
  int index;
  for(int i=0; i<1000001; i++){
    if(input_exp[i] !=0){
      index = i;
      gcd_exp = input_exp[i]/n;

      for(int j=0; j<n; j++){
        for(auto k = v[j].begin(); k!=v[j].end(); k++) {
          if (k->first == index){
            while (k->second > gcd_exp){
              k->second--;
              cnt ++;
            }
          }
        } 
      }
      for(int j=0; j<gcd_exp; j++) {
        score *= index;
      }
      int duplicate_cnt = input_exp[i]%n;
      cnt -=duplicate_cnt;
    }
  }
  printf("%d %d", score, cnt);
}

int main(){
	input();
	init();
  isPrimeNum();
	factorization();
	output();
	return 0;
}