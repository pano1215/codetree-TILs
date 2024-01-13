// 변수 선언 및 입력
const fs = require("fs");

// 배열에 정수들을 입력 받습니다.
let arr = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let max_val = Number.MIN_SAFE_INTEGER ;

for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= max_val) {
        max_val = arr[i] ;
    }
}

console.log(max_val) ;