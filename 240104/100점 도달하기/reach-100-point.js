// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());
let result = "";

// 출력
for (let i = n; i <= 100; i++) {
    if (i >= 90) {
        result += "A ";
    }
    else if (i >= 80) {
        result += "B ";
    }
    else if (i >= 70) {
        result += "C ";
    }
    else if (i >= 60) {
        result += "D ";
    }
    else {
        result += "F ";
    }
}

console.log(result);