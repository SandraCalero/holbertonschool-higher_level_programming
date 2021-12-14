#!/usr/bin/node
/// This script is printing the addition of 2 integers
function add (a, b) {
  return a + b;
}

const process = require('process');
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);
const result = add(num1, num2);
console.log(result);
