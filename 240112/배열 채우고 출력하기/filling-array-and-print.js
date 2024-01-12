// 배열을 구현하여 주어진 수를 입력받습니다.
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let leng = input.length ;
let result = "" ;

for (let i = leng - 1; i > -1; i--) {
    result += input[i]
}

console.log(result) ;