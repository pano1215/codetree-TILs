const fs = require("fs");

let ft = fs.readFileSync(0).toString();
ft = Number(ft);

let cm = ft * 30.48 ;

console.log(cm.toFixed(1)) ;