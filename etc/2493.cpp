
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
using std::make_pair;
using std::pair;
using std::vector;
using pii=pair<int,int>;
using lint=long long;
int tower[500001];
int n;
vector<pii> v;

void input(){
  scanf("%d", &n);
}

int findConnectedTower(int cur) {
  if (v.empty()) {
    v.push_back(std::make_pair(cur, tower[cur]));
    return 0;
  }

  while (!v.empty()) {
    if (v.back().second >= tower[cur]) {
      int res = v.back().first;
      v.push_back(std::make_pair(cur, tower[cur]));
      return res;
    }
    else v.pop_back();
  }

  v.push_back(std::make_pair(cur, tower[cur]));

  return 0;
}

void init(){
  for (int i=1; i<=n; i++) {
    scanf("%d", &tower[i]);
    printf("%d ", findConnectedTower(i));
  }
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