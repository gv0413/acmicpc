const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
rl.on('line', input=> {
  for(let i=1; i<=input; i++){
    console.log(i);
  }
}).on('close', () => {
  process.exit();
})
// 시간초과 