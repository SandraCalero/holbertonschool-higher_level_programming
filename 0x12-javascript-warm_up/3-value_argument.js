#!/usr/bin/node
/// This script is printing the first argument passed to it
const process = require('process');
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
