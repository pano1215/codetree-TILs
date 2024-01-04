// 입력 및 변수 선언
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let height = Number(input[0]) / 100;
let weight = Number(input[1]);

// BMI 계산
let bmi = parseInt(weight / (height ** 2));

// 출력
console.log(bmi);
if (bmi >= 25) {
    console.log("Obesity");
}