#!/usr/bin/node
/// This script is searching the second biggest integer in the list of arguments
const process = require('process');
const array = process.argv.slice(2, process.argv.length);
const arrayLen = array.length;
if (arrayLen <= 1) {
  console.log('0');
} else {
  array.sort();
  for (let idx = arrayLen - 2; idx >= 0; idx--) {
    if (array[idx] < array[idx + 1]) {
      console.log(parseInt(array[idx]));
      break;
    }
  }
}
