#!/usr/bin/node
// This script is writing a string to a file.
const filePath = process.argv[2];
const stringToWrite = process.argv[3];
const fs = require('fs');
fs.writeFile(filePath, stringToWrite, function (err) {
  if (err) return console.log(err);
});
