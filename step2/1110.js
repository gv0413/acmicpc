const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', input => {
  let number = Number.parseInt(input);
  var count = 0;
  for(;;){
    number = getValue(number);
    count++;

    if(input==number)
    break;
  }
  console.log(count);
})

function getValue(input){
  const a = Math.floor(input/10);
  const b = input - 10 * a;
  const sum = a + b;
  const value = 10 * b + (sum - 10 * Math.floor(sum/10));
  
  return value;
}