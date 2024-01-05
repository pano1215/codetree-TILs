// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().split(" ");
let a = Number(input[0]);
let b = Number(input[1]);
let prod = 1;

// 1부터 b까지의 a의 배수들을 곱합니다.
for (let i = 1; i <= b; i++) {
    if (i % a === 0) {
        prod *= i;
    }
}

// 출력
console.log(prod);