// 2차원 배열을 구현합니다.
let arr = Array(5).fill(0).map(() => Array(5).fill(0));

// 배열의 첫 행과 첫 열을 1로 초기화합니다.
for (let i = 0; i < 5; i++) {
    arr[i][0] = 1;
    arr[0][i] = 1;
}

// 배열의 숫자를 채웁니다.
for (let i = 1; i < 5; i++) {
    for (let j = 1; j < 5; j++) {
        arr[i][j] = arr[i][j - 1] + arr[i - 1][j];
    }
}

// 채워진 배열을 출력합니다.
for (let i = 0; i < 5; i++) {
let str = "";
    for (let j = 0; j < 5; j++) {
        str += arr[i][j] + " ";
    }
    console.log(str);
}