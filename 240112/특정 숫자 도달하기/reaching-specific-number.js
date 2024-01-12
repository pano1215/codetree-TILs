// 배열을 구현하여 주어진 수를 입력받습니다.
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");
input = input.map(Number) ;

let sum_val = 0 ;
let cnt = 0 ;

for (let e of input) {
    if (e >= 250) {
        break ;
    }
    sum_val += e ;
    cnt++ ;
}

let result = sum_val / cnt ;
console.log(sum_val, result.toFixed(1)) ;