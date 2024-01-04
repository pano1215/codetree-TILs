// 변수 선언 및 입력
const fs = require("fs");
let input = Number(fs.readFileSync(0).toString().trim());

// 출력
if (input === 1) {
    console.log("John");
}
else if (input === 2) {
    console.log("Tom");
}
else if (input === 3) {
    console.log("Paul");
}
else {
    console.log("Vacancy");
}