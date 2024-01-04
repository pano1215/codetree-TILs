// 입력 및 변수 선언
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let a = Number(input[0]);
let b = Number(input[1]);

// 평균 구하기
let average = (a + b) / 2;

// 출력
console.log(a + b, average.toFixed(1));