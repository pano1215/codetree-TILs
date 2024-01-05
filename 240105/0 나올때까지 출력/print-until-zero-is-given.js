// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let index = 0;

// 언제 끝날지 모르므로
// 계속 반복합니다.
while (true) {
    // 입력을 받습니다.
    let n = Number(input[index]);
    index++;
    // 입력받은 값이 0이면 종료합니다.
    if (n === 0) {
        break;
    }

    // n이 0이 아닌 경우에는, 계속 값을 출력해줍니다.
    console.log(n);
}