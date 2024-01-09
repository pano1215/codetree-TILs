// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

let satisfied = true;

for (let i = 2; i < n; i++) {
    // a에서 b 사이의 값 중 c의 배수가 있는지 확인합니다.
    if (n % i === 0) {
        satisfied = false;
    }
}

// 출력
if (satisfied === true) {
    console.log("P");
}
else {
    console.log("C");
}