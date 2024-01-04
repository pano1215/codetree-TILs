// 입력 및 변수 선언
let fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let a = Number(input[0]);
let b = Number(input[1]);

// 출력
if (a % 2 === 0) {
    console.log("even");
} 
else {
    console.log("odd");
}

if (b % 2 === 0) {
    console.log("even");
} 
else {
    console.log("odd");
}