const fs = require("fs") ;
let input = fs.readFileSync(0).toString().trim().split("\n") ;

let n = Number(input[0]) ;

let cnt = 0;
for (let i = 1; i <= n; i++) {
    let reault = 0 ;
    let arr = input[i].split(" ") ;
    arr = arr.map(Number) ; 

    for (let i of arr) {
        reault += i ;
    }

    let avg = reault / 4 ;
    if (avg >= 60){
        console.log("pass") ;
        cnt++ ;
    }
    else {
        console.log("fail") ;
    }
}
console.log(cnt) ;