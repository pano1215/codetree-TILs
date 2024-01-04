// 입력 및 변수 선언
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim();

let n = Number(input);

// 출력
console.log(n ** 2)
if (n < 5) console.log("tiny");