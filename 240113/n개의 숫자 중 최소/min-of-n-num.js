// 변수 선언 및 입력
const fs = require("fs");

// 배열에 정수들을 입력 받습니다.
let input = fs.readFileSync(0).toString().trim().split("\n");
let n = Number(input[0]);
let arr = input[1].split(" ").map(Number);

let min_val = Number.MAX_SAFE_INTEGER ;
for (let i of arr) {
    if (i <= min_val){
        min_val = i ;
    }
}

let cnt = 0 ;
for (let i of arr) {
    if (i == min_val){
        cnt++ ;
    }
}

console.log(min_val, cnt) ;