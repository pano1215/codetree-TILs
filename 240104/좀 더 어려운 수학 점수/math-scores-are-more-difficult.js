// 입력 및 변수 선언
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let scoreA = input[0].split(" ");
let scoreB = input[1].split(" ");

let mathA = Number(scoreA[0]), engA = Number(scoreA[1]);
let mathB = Number(scoreB[0]), engB = Number(scoreB[1]);

// 출력
if (mathA > mathB || (mathA == mathB && engA > engB)) {
    console.log("A");
} 
else {
    console.log("B");
}