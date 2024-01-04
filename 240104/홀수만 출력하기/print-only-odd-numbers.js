// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");
let n = Number(input[0]);

// 출력
for (let i = 1; i <= n; i++) {
    // x는 i번째 숫자를 의미합니다.
    let x = Number(input[i]);

    if (x % 2 === 1 && x % 3 === 0) {
        console.log(x);
    }
}