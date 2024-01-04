// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim();

let a = Number(input);

let result = a === 100 ? "pass" : "failure";

// 출력
console.log(result);