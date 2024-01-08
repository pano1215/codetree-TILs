// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());
let cnt = 1;
let prod = 2;

while (true) {
    // prod가 n이 될 때까지 2를 곱합니다.
    if (prod === n) {
        break;
    }    
    
    prod *= 2;
    cnt++;
}

console.log(cnt);