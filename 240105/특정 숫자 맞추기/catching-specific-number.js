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
    // n이 25보다 작으면 Higher을, 25보다 크면 Lower을
    // 25와 같으면 Good을 출력한 뒤 종료합니다.
    if (n < 25) {
        console.log("Higher");
    }
    else if (n > 25) {
        console.log("Lower");
    }
    else {
        console.log("Good");
        break;
    }
}