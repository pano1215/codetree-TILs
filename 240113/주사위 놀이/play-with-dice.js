// 변수 선언 및 입력
const fs = require("fs");
let arr = fs.readFileSync(0).toString().trim().split(" ") ;
arr = arr.map(Number) ;

let result_arr = Array(7).fill(0) ;

for (let i of arr) {
    result_arr[i]++ ;
}

// 1부터 9까지 나온 횟수를 출력
for (let i = 1; i < 7; i++) {
    console.log(i, "-", result_arr[i]);
}