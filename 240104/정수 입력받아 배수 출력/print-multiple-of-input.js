// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

// 출력
let result = "";
for (let i = n; i <= n * 5; i += n) {
    result += i + " ";
}
console.log(result);