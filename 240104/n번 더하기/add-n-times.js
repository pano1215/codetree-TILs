// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");
let a = Number(input[0]);
let n = Number(input[1]);

// 출력
for (let i = 0; i < n; i++) {
    a += n;
    console.log(a);
}