// 입력 및 변수 선언
const fs = require("fs");
let y = Number(fs.readFileSync(0).toString().trim().split("\n"));

// 출력
if ((y % 4 == 0 && y % 100 != 0) || y % 400 == 0) {
    console.log("true");
}
else {
    console.log("false");
}