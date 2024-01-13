const fs = require("fs") ;
let arr = fs.readFileSync(0).toString().trim().split(" ") ;
arr = arr.map(Number) ;

let sec_arr = [] ;

for (let i of arr) {
    if (i == 0) break ;

    sec_arr.push(i) ;
}

let reault = 0 ;
let cnt = 0 ;
for (let i of sec_arr) {
    if (i % 2 == 0){
        reault += i ; // 합
        cnt++ ;
    }
}

console.log(cnt, reault) ;