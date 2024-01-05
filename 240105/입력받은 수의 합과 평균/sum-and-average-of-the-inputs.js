// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().split("\n");
let n = Number(input[0]);
let sumVal = 0;

// 합을 구합니다.
for (let i = 1; i <= n; i++) {
    sumVal += Number(input[i]);
}

// 평균을 구합니다.
let avg = sumVal / n;

// 출력
console.log(sumVal, avg.toFixed(1));