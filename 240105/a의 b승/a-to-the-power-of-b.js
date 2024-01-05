// 변수 선언 및 입력
const fs = require("fs") ;
let input = fs.readFileSync(0).toString().split(" ") ;
let a = Number(input[0]) ;
let b = Number(input[1]) ;
let start_num = 1 ; 

// a부터 b까지의 수들을 곱합니다.
for (let i = 0; i < b; i++) {
    start_num *= a ;
}

// 출력
console.log(start_num);