// 변수 선언, 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");
let s = input[0];
let t = input[1];

// 값 교체
[s, t] = [t, s]

// 출력
console.log(s)
console.log(t)