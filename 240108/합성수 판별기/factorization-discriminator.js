// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());
let satisfied = false;

for (let i = 2; i < n; i++) {
    // n의 약수가 있다면 합성수입니다.
    if (n % i === 0) {
        satisfied = true;
    }
}

// 출력
if (satisfied === true) {
    console.log("C");
}
else {
    console.log("N");
}