#!/usr/bin/node
/// This script is printing My number: <first argument converted in integer> if the first argument can be converted to an integer
const process = require('process');
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number:', num);
}
