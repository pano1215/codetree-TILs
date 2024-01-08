// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());
let cnt = 0;

while (true) {
    // n이 1000이 될 때까지 연산을 반복합니다.
    if (n % 2 === 0) {
        n = n * 3 + 1;
    }
    else {
        n = n * 2 + 2;
    }

    cnt++;
    if (n >= 1000) {
        break;
    }
}

console.log(cnt);