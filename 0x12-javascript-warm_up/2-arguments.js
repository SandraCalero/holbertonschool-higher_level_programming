#!/usr/bin/node
/// This script is printing a message depending of the number of arguments passed
const process = require('process');
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
