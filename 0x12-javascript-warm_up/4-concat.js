#!/usr/bin/node
/// This script is printing two arguments passed to it, in the following format: “ is ”
const process = require('process');
console.log(process.argv[2], 'is', process.argv[3]);
