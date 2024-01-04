// 입력 및 변수 선언
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let a = Number(input[0]);
let b = Number(input[1]);
let c = Number(input[2]);

// 출력
if (a > b) {
    if (c > a) {
        // a > b, c > a 일때 (c > a > b)
        console.log(a);
    }
    // a > b, a > c 일때 (a가 가장 크고, b와 c중 더 큰 수가 중앙값)
    else if (b > c) {
        console.log(b);
    }
    else {
        console.log(c);
    }
}
else {
    if (c > b) {
        // b > a, c > b 일때 (c > b > a)
        console.log(b);
    }
    // b > a, b > c 일때 (b가 가장 크고, a와 c중 더 큰 수가 중앙값)
    else if (a > c) {
        console.log(a);
    }
    else {
        console.log(c);
    }
}