// readline으로 하려고 했으나 입력값을 따로 관리할 수 없어 fs이용
var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');
var a = parseInt(input[0]);
var i = 1;

for(i=1; i<=a; i++){
  var arr = input[i].split(' ');
  var b = arr[0];
  var c = arr[1];
  console.log(+b + +c);
}
