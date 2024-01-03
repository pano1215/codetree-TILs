// 변수 선언, 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("-");

// 값 변경
[input[1], input[2]] = [input[2], input[1]];

// 출력
console.log(`${input[0]}-${input[1]}-${input[2]}`);