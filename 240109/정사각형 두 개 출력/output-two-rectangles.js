// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

let str = "";

// n * n 크기의 별을 출력합니다.
for (let i = 0; i < n; i++) {
    str = "";
    for (let j = 0; j < n; j++) {
        str += "*";
    }
    console.log(str);
}

console.log();

// n * n 크기의 별을 한번 더 출력합니다.
for (let i = 0; i < n; i++) {
    str = "";
    for (let j = 0; j < n; j++) {
        str += "*";
    }
    console.log(str);
}