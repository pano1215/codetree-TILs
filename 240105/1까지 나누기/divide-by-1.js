// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());
let cnt = 0;

// 1부터 증가시키며 나눈 값이 1이하가 된 순간, 나눗셈을 진행한 횟수를 출력합니다.
for (let i = 1; i <= 100; i++) {
    n = parseInt(n / i);
    cnt++;
    if (n <= 1) {
        break;
    }
}

console.log(cnt);