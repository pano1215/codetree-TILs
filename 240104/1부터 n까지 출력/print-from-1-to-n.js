// 입력 및 변수 선언
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

// 출력
let result = "";
for (let i = 1; i <= n; i++) {
    result += (i + " ");
}

console.log(result);