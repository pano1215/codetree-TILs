// 변수 선언 및 입력
const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());
let sumVal = 1 ;

// 1부터 증가시키며 더한 값이 n이상이 된 순간, 더해진 숫자를 출력합니다.
for (let i = 1; i <= 10; i++) {
    sumVal *= i;
    if (sumVal >= n) {
        console.log(i);
        break;
    }
}