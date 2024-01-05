// 변수 선언 및 입력
const fs = require("fs") ;
let n = Number(fs.readFileSync(0).toString().trim()) ;
let i = 1 ;
let sum_val = 0 ;

for (; i <= 100; i++) {
    sum_val += i ;

    if (sum_val >= n) {
        break ;
    }
}

console.log(i) ;