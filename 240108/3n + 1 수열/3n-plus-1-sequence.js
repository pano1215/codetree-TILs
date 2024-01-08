// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());
let cnt = 0;

while (true) {
    // n이 1이 될 때까지 홀수일 때는 n = 3n + 1을
    // 짝수일 때는 n = n / 2를 반복합니다.
    if (n === 1) {
        break;
    }

    if (n % 2 === 0) {
        n = n / 2;
    }
    else {
        n = 3 * n + 1;
    }
    cnt++;
}

console.log(cnt);