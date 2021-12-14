#!/usr/bin/node
/// This script is searching the second biggest integer in the list of arguments
const process = require('process');
const array = [];
const arrayLen = process.argv.length;
if (arrayLen <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < arrayLen; i++) {
    array.push(process.argv[i]);
  }
  array.sort();
  for (let idx = array.length - 2; idx >= 0; idx--) {
    if (array[idx] < array[idx + 1]) {
      console.log(array[idx]);
      break;
    }
  }
}
