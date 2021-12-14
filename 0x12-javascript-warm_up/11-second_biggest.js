#!/usr/bin/node
/// This script is searching the second biggest integer in the list of arguments
const process = require('process');
const array = process.argv.slice(2, process.argv.length);
const arrayLen = array.length;
if (arrayLen <= 1) {
  console.log(0);
} else {
  array.sort();
  console.log(parseInt(array[arrayLen - 2]));
}
