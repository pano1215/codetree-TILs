// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);
let k = 0;

// 0이 입력될 때까지 100개의 정수를 배열에 입력받아 저장합니다.
for (let i = 0; i < 100; i++) {
    if (input[i] === 0) {
        k = i;
        break;
    }
}

// 출력
console.log(input[k - 3] + input[k - 2] + input[k - 1]);