const fs = require("fs") ;
let input = fs.readFileSync(0).toString().trim() ;
let n = Number(input) ;
let result = "" ;

for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
        continue ;
    }
    else if (i % 10 === 5) {
        continue ;
    }
    else if (i % 3 === 0 && i % 9 != 0) {
        continue ;
    }
    result += i + " " ;
}

console.log(result) ;