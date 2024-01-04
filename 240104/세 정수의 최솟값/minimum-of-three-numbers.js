// 입력 및 변수 선언
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let a = Number(input[0]);
let b = Number(input[1]);
let c = Number(input[2]);

// 출력
let minNumber;
if (a <= b && a <= c) minNumber = a;
else if (b <= a && b <= c) minNumber = b;
else minNumber = c;

console.log(minNumber);