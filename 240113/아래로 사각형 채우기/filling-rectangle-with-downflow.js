// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

// 2차원 배열을 구현합니다.
let arr = Array(n).fill(0).map(() => Array(n).fill(0));

// 배열의 숫자를 채웁니다.
let num = 1;
for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
        arr[j][i] = num;
        num++;
    }
}

// 채워진 배열을 출력합니다.
for (let row of arr) {
    let str = "";
    for (let elem of row) {
        str += elem + " ";
    }
    console.log(str);
}