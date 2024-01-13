// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let n = Number(input[0]);

// n개의 정수를 배열에 입력받아 저장합니다.
let arr = input[1].split(" ").map(Number);

// 배열 선언
let newArr = [];

for (let i = 0; i < n; i++) {
    newArr[i] = arr[i] * arr[i];
}

// n개의 정수를 출력합니다.
let str = "";
for (let i = 0; i < n; i++) {
    str += newArr[i] + " ";
}

console.log(str);