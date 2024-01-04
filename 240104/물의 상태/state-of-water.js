// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim();

let a = Number(input);

// 출력
if (a < 0) {
    console.log("ice");
}
else if (a >= 100) {
    console.log("vapor");
}
else {
    console.log("water");
}