const fs = require("fs") ;
let arr = fs.readFileSync(0).toString().trim().split(" ").map(Number) ;

let result = 0 ;
let three_sum = 0 ;
let three_cnt = 0 ;
for (let i = 0; i < 10; i++) {
    if (i % 2 == 1) {
        result += arr[i] ;
    }
    if (i % 3 == 0 && i != 0) {
        three_sum += arr[i - 1] ;
        three_cnt++ ;
    }
}

let three_avg = three_sum / three_cnt ;
console.log(result, three_avg.toFixed(1)) ;  //.toFixed(1)) ;