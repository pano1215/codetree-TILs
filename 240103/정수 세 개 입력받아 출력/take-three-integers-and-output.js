// 변수 선언, 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

// 첫번째 줄은 공백으로 나눠져 있기 때문에
// 한번 더 split을 해줍니다.
let arr = input[0].split(" ")
let a = Number(arr[0]);
let b = Number(arr[1]);
let c = Number(input[1]);

// 출력
console.log(a, b, c);