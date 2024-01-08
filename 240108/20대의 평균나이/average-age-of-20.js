// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let sumVal = 0, cnt = 0;

// 언제 끝날지 모르므로
// 계속 반복합니다.
while (true) {
    // 입력을 받습니다.
    let n = Number(input[cnt]);
    
    if (parseInt(n / 10) !== 2) {
        console.log((sumVal / cnt).toFixed(2));
        break;
    }
    
    sumVal += n;
    cnt++;
}