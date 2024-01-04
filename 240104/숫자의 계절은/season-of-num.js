// 입력 및 변수 선언
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

// 출력
if (n >= 12 || n <= 2) {
    console.log("Winter");
}
else if (n <= 5) {
    console.log("Spring")
}
else if (n <= 8) {
    console.log("Summer");
}
else {
    console.log("Fall");
}