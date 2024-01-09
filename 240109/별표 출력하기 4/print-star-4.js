// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

let str = "";

// 길이가 n인 직각삼각형을 뒤집어 출력합니다.
for (let i = n - 1; i >= 0; i--) {
    str = "";
    for (let j = 0; j <= i; j++) {
        str += "* ";
    }
    console.log(str);
}

// 길이가 n-1인 직각삼각형을 출력합니다.
for (let i = 1; i < n; i++) {
    str = "";
    for (let j = 0; j <= i; j++) {
        str += "* ";
    }
    console.log(str);
}