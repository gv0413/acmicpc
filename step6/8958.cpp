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
char arr [81];
void input(){
  scanf("%d", &n);
  for(int i=0; i<n; i++){
    int sum = 0;
    int score = 1;
    scanf("%s", &arr);
    for(int j=0; j<strlen(arr); j++){
      if(arr[j]=='O'){
        sum += score;
        score++;
      }
      if(arr[j]=='X'){
        score=1;
      }
    }
    printf("%d\n", sum);
  }
}

void process(){
}

void output(){

}

int main(void){
	input();
	process();
	output();
	return 0;
}