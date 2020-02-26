const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', input => {
    
  multiplication(input);

}).on('close', () => {
    process.exit();
});

function multiplication(n){
  for(let i=1;i<=9;i++){
    console.log( n, "*",i, "=" ,n*i);
  }
}
