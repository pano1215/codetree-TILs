// 입력 및 변수 선언
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

// 출력
if (n === 2) {
    console.log(28);
}
else if (n <= 7) {
    if (n % 2 === 1) {
        console.log(31);
    }
    else {
        console.log(30);
    }
}
else {
    if (n % 2 === 0) {
        console.log(31);
    }
    else {
        console.log(30);
    }
}