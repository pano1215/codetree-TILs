let word = ['L', 'E', 'B', 'R', 'O', 'S'] ;

// 변수 선언 및 입력
const fs = require("fs") ;
let chr = fs.readFileSync(0).toString().trim() ;
let idx = -1 ; 

function Letter(chr) {
    for (let i = 0; i < word.length; i++) {
        if (word[i] == chr) {
            idx = i ;
        }
    }

    if (idx == -1) {
        return "None" ;
    }
    else {
        return idx ;
    }
}

console.log(Letter(chr)) ;