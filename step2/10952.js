const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', input => {
    const arr = input.split(' ');
    const a = Number.parseInt(arr[0]);
    const b = Number.parseInt(arr[1]);
    
    if(a===0  && b===0) {
      rl.close();
    }
    console.log(a+b);
}).on('close', () => {
    process.exit();
});