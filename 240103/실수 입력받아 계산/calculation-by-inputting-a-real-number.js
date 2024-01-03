const fs = require("fs");
let input = fs.readFileSync(0).toString().split("\n");

let a = input[0];
let b = input[1];
let re = Number(a + b) ;

console.log(re.toFixed(2));