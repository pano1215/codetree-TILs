// 변수 선언, 입력
const fs = require("fs");
let a = Number(fs.readFileSync(0).toString());

// 출력
console.log(a * 2);