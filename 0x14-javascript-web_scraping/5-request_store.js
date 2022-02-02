#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file
const request = require('request');
const requestUrl = process.argv[2];
const filePath = process.argv[3];

request(requestUrl, function (error, body) {
  if (error) {
    console.log(error);
  } else {
    const fs = require('fs');
    fs.writeFile(filePath, body.body, 'utf-8', function (err) {
      if (err) return console.log(err);
    });
  }
});
