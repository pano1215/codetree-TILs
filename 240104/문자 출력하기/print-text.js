// 변수 선언 및 입력
const fs = require("fs");
let n = fs.readFileSync(0).toString().trim();

// 출력
let result = "";
for (let i = 0; i < 8; i++) {
    result += n;
}
console.log(result);