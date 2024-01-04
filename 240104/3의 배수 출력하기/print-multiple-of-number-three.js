// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());
let result = "";

let i = 3;

// 출력
while (i <= n) {
    result += i + " ";
    i += 3;
}

console.log(result);