// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");
let cnt = 0;

for (let i = 0; i < 5; i++) {
    if (input[i] % 2 === 0) {
        cnt++;
    }
}

// 출력
console.log(cnt);