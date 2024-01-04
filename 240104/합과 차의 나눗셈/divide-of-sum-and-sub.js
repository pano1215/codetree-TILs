// 입력 및 변수 선언
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let a = Number(input[0]);
let b = Number(input[1]);

// 연산 진행
let plus = a + b;
let minus = a - b;

// 출력
console.log((plus / minus).toFixed(2));