const fs = require("fs") ;
let input = fs.readFileSync(0).toString().trim().split("\n") ;
let n = Number(input[0]) ;
let arr = input[1].split(" ").map(Number) ;

let result = "" ;
for (let i = arr.length - 1; i >= 0; i--) {
    if(arr[i] % 2 == 0) {
        result += arr[i] + " " ;
    }
}

console.log(result) ;