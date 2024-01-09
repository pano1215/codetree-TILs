// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

let str = "";

// Step 1:
for (let i = 1; i <= n; i++) {
    str = "";

    for (let j = 0; j < n - i; j++) {
        str += " ";
    }

    for (let j = 0; j < 2 * i - 1; j++) {
        str += "*";
    }

    for (let j = 0; j < n - i; j++) {
        str += " ";
    }

    console.log(str);
}   

// Step 2:
for (let i = n - 1; i >= 1; i--) {
    str = "";

    for (let j = 0; j < n - i; j++) {
        str += " ";
    }

    for (let j = 0; j < 2 * i - 1; j++) {
        str += "*";
    }

    for (let j = 0; j < n - i; j++) {
        str += " ";
    }

    console.log(str);
}