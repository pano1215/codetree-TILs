// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let n = Number(input[0]) ;
let arr = input[1].split(" ").map(Number) ;
let result_arr = Array(11).fill(0) ;

for (let i of arr) {
    result_arr[i - 1]++ ;
}

// 1부터 9까지 나온 횟수를 출력
for (let i = 0; i < 9; i++) {
    console.log(result_arr[i]);
}