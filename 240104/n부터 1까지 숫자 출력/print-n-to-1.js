// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

// 출력
let result = "";
while (n >= 1) {
    result += n + " ";
    n--;
}
console.log(result);