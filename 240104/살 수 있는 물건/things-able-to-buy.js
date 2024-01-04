// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim();

let n = Number(input);

// 출력
if (n >= 3000) {
    console.log("book");
}
else if (n >= 1000) {
    console.log("mask");
}
else {
    console.log("no");
}