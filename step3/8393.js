const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
rl.on('line', input=> {
  let sum=0;
  for(let i=0; i<=input; i++){
    sum = sum+i;
  }
  console.log(sum);
}).on('close', () => {
  process.exit();
})