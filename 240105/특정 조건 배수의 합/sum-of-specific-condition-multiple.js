// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");
let a = Number(input[0]);
let b = Number(input[1]);
let sumVal = 0;

if (a < b) {
    for (let i = a; i <= b; i++) {
        if (i % 5 === 0) {
            sumVal += i;
        }
    }
}
else {
    for (let i = b; i <= a; i++) {
        if (i % 5 === 0) {
            sumVal += i;
        }
    } 
}

// 출력
console.log(sumVal);