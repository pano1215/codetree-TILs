const fs = require("fs") ;
let input = Number(fs.readFileSync(0).toString().trim()) ;
sum_num = 0 ;

for (let i = input; i <= 100; i++){
    sum_num += i ;
}

console.log(sum_num) ;