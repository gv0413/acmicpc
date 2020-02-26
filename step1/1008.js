const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', input => {
    const arr = input.split(' ');
    const a = arr[0];
    const b = arr[1];
    console.log(a/b);
    rl.close();
}).on('close', () => {
    process.exit();
});