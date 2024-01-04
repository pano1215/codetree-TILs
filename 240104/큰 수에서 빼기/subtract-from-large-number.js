// 입력 및 변수 선언
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");
let a = Number(input[0]);
let b = Number(input[1]);

// 출력
if (a >= b) {
    console.log(a - b);
}

if (a < b) {
    console.log(b - a);
}