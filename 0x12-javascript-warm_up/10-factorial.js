#!/usr/bin/node
/// This script is computing and prints a factorial
function factorial (num) {
  if (num <= 0) {
    return 1;
  }
  return num * factorial(num - 1);
}

const process = require('process');
const num = parseInt(process.argv[2]);
let result = 1;
if (!isNaN(num)) {
  result = factorial(num);
}
console.log(result);
