// 변수 선언 및 입력
const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split(" ");
let a = Number(input[1]);
let b = Number(input[0]);

// 출력
let result = "";
for (let i = b; i >= a; i -= 2) {
    result += i + " ";
}
console.log(result);