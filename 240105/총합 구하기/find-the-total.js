// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().split(" ");
let a = Number(input[0]);
let b = Number(input[1]);
let sumVal = 0;

// a부터 b까지 조건을 만족하는 수를 더합니다.
for (let i = a; i <= b; i++) {
    if (i % 6 === 0 && i % 8 !== 0) {
        sumVal += i;
    }
}

// 출력
console.log(sumVal);