// 입력 및 변수 선언
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let a = Number(input[0]);
let b = Number(input[1]);
let c = Number(input[2]);

// 평균과 총합 구하기
// 소수점을 버려야하기 때문에 parseInt()를 사용합니다.
let total = a + b + c;
let average = parseInt(total / 3);


// 출력
console.log(total);
console.log(average);
console.log(total - average);