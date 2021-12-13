#!/usr/bin/node
/// This script is printing a message depending of the number of arguments passed
const process = require('process');
if (process.argv.length <= 2) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
