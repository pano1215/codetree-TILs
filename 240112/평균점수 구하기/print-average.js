const fs = require("fs") ;
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number) ;
//input = input.map(Number) ;

let total = 0 ;

for (let e of input) {
    total += e ;
}
let result = total / 8 ;
console.log(result.toFixed(1)) ;