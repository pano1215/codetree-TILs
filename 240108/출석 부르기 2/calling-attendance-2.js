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

    // n이 1~4라면 번호에 맞는 이름을, 그게 아니라면 Vacancy를 출력한 뒤 종료합니다.
    if (n === 1) {
        console.log("John");
    }
    else if (n === 2) {
        console.log("Tom");
    }
    else if (n === 3) {
        console.log("Paul");
    }
    else if (n === 4) {
        console.log("Sam");
    }
    else {
        console.log("Vacancy");
		break;
    }
}