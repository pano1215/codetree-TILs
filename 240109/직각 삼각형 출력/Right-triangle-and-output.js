// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

let str = "";

// 길이가 n인 직각삼각형을 출력합니다.
for (let i = 0; i < n; i++) {
    str = "";
    // i번째 행에는 2 * i + 1개의 별이 있습니다.
    for (let j = 0; j < 2 * i + 1; j++) {
        str += "*";
    }
    // 행마다 한 줄씩 띄워줍니다.
    console.log(str);
}