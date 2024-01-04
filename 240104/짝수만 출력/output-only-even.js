// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");
let a = Number(input[0]);
let b = Number(input[1]);

let result = "";

// 출력
while (a <= b) {
    result += a + " ";
    a += 2;
}

console.log(result);