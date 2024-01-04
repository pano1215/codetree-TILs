// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

// 출력
let result = "";
for (let i = 1; i <= n; i++) {
    if (i % 3 === 0) {
        result += "0 ";
    }
    else if (i % 10 === 3 || i % 10 === 6 || i % 10 === 9) {
        result += "0 ";
    }
    else if (parseInt(i / 10) === 3 || parseInt(i / 10) === 6 || parseInt(i / 10) === 9) {
        result += "0 ";
    }
    else {
        result += i + " ";
    }
}

console.log(result);