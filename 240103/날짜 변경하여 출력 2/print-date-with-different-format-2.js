// 변수 선언, 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("-");
let m = Number(input[0]);
let d = Number(input[1]);
let y = Number(input[2]);

// 출력
console.log(`${y}.${m}.${d}`);