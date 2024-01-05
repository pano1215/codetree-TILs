// 변수 선언 및 입력
const fs = require("fs");
let a = Number(fs.readFileSync(0).toString().trim());
let result = "";

// 조건을 모두 만족하지 않는 수들만 출력합니다.
for (let i = 1; i <= a; i++) {
    if ((i % 2 === 0 && i % 4 !== 0) || (parseInt(i / 8) % 2 === 0) || i % 7 < 4) {
        continue;
    }
    result += i + " ";
}

// 출력
console.log(result);