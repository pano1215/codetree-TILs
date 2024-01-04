// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim();

let n = Number(input);

// 출력
if (n >= 113) {
    console.log(1);
}
else {
    console.log(0);
}