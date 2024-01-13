const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let arr = [] ;

for (let i of input) {
    let sum_val = 0 ;
    i = i.split(" ").map(Number) ;
    for (let j of i) {
        sum_val += j ;
    }
    console.log(sum_val) ;
}