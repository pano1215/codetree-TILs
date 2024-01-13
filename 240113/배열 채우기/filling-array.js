const fs = require("fs") ;
let arr = fs.readFileSync(0).toString().trim().split(" ") ;
arr = arr.map(Number) ;

let sec_arr = [] ;

for (let i of arr) {
    if (i == 0) {
        break ;
    }

    sec_arr.push(i) ;
}

let reault = "" ;
for (let i = sec_arr.length - 1; i >= 0; i--) {
    reault += sec_arr[i] + " " ;
}
console.log(reault) ;