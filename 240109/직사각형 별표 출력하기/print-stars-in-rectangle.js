// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");
let n = input[0] ;
let m = input[1] ;

// n * n 크기의 별을 출력합니다.
let str = "";
for (let i = 0; i < n; i++) {
    str = "";
    for (let j = 0; j < m; j++) {
        str += "* ";
    }
    console.log(str);
}