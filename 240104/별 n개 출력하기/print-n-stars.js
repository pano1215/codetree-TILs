// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

let i = 1;

// 출력
while (i <= n) {
    console.log("*");
    i++;
}