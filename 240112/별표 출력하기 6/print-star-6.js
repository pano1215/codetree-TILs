const fs = require("fs") ;
let n = Number(fs.readFileSync(0).toString().trim()) ;

let str = "" ;

for(let i = 0; i < n; i++) {
    str = "" ;

    // 윗 삼각형
    for (let j = 0; j < i; j++) {
        str += "  " ;
    }
    for (let j = 0; j < (2 * n) - 1 - (2 * i); j++) {
        str += "* " ;
    }
    console.log(str) ; 
}

// 아래 삼각형
for(let i = 1; i < n; i++) {
    str = "" ;

    for (let j = 0; j < (n - 1 - i); j++) {
        str += "  " ;
    }
    for (let j = 0; j < 1 + (2 * i); j++) {
        str += "* " ;
    }
    console.log(str) ; 
}