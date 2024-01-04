// 입력 및 변수 선언
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let a = Number(input[0]);
let b = Number(input[1]);
let c = Number(input[2]);

// 평균 구하기
// 소수점을 버려야하기 때문에 parseInt()를 사용합니다.
let average = parseInt((a + b + c) / 3);

// 출력
console.log(a + b + c)
console.log(average);