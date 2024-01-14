function cmp(prev, cur) {
    if (prev > cur) return 1;
    else if (prev < cur) return -1;
    return 0;
}

// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");
let n = Number(input[0]) ;
let arr = input[1].trim().split(" ").map(Number) ;

let sort_arr = arr.sort(cmp) ;
let sort_result = "" ;
for (let i of sort_arr) {
    sort_result += i + " " ;
}
console.log(sort_result) ;

let reverse_arr = arr.reverse() ;
let reverse_result = "" ;
for (let i of reverse_arr) {
    reverse_result += i + " " ;
}
console.log(reverse_result) ;