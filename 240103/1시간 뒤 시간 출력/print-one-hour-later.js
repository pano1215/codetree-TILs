const fs = require("fs");
let input = fs.readFileSync(0).toString().trim();
let arr = input.split(":") ;
console.log("%d:%s", Number(arr[0]) + 1, arr[1])