const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', input => {
    const arr = input.split(' ');
    const a = Number.parseInt(arr[0]);
    const b = Number.parseInt(arr[1]);
    
    console.log(a+b);
})