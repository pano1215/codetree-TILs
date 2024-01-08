// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let index = 0;

// 언제 끝날지 모르므로
// 계속 반복합니다.
while (true) {
    // 입력을 받습니다.
    let arr = input[index].split(" ");
    let x = Number(arr[0]);
    let y = Number(arr[1]);
    let c = arr[2];

    index++;
    
    // 사각형의 넓이를 출력합니다. 문자 C가 입력되면 종료합니다.
    console.log(x * y);

    if (c === "C") {
        break;
    }
}