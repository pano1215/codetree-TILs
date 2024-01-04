// 입력 및 변수 선언
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let middleScore = Number(input[0]);
let finalScore = Number(input[1]);

// 출력
if (middleScore >= 90 && finalScore >= 95) {
    console.log(100000);
}
else if (middleScore >= 90 && finalScore >= 90) {
    console.log(50000)
}
else {
    console.log(0);
}