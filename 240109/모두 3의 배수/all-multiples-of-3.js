// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");
let satisfied = true;

for (let i = 0; i < 5; i++) {
    // 모든 수가 3의 배수인지 확인합니다.
    let number = Number(input[i]);
    if (number % 3 !== 0) {
        satisfied = false;
    }
}

// 출력
if (satisfied === true) {
    console.log(1);
}
else {
    console.log(0);
}