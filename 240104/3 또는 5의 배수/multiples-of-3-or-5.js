// 입력 및 변수 선언
let fs = require("fs");
let a = Number(fs.readFileSync(0).toString().trim());

// 출력
if (a % 3 === 0) {
    console.log("YES")
} 
else {
    console.log("NO");
}

if (a % 5 === 0) {
    console.log("YES")
} 
else {
    console.log("NO");
}