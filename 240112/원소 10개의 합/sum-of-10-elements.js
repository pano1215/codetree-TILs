const fs = require("fs") ;
let arr = fs.readFileSync(0).toString().trim().split(" ") ;

arr = arr.map(Number);
let leng = arr.length ;
let result = 0 ;

for (let i = 0; i < leng; i++) {
    result += arr[i]
}
console.log(result) ;