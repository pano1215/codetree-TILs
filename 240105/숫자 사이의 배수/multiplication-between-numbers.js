// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");
let a = Number(input[0]);
let b = Number(input[1]);
let sumVal = 0, cnt = 0;

for (let i = a; i <= b; i++) {
    if (i % 5 === 0 || i % 7 === 0) {
        sumVal += i;
        cnt++;
    }
}

// 출력
console.log(sumVal, (sumVal / cnt).toFixed(1));