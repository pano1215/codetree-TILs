// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");
let a = Number(input[0]);
let b = Number(input[1]);
let c = Number(input[2]);

let satisfied = false;

for (let i = a; i <= b; i++) {
    // a에서 b사이의 값 중 c의 배수가 있는지 확인합니다.
    if (i % c === 0) {
        satisfied = true;
    }
}

// 출력
if (satisfied === true) {
    console.log("YES");
}
else {
    console.log("NO");
}