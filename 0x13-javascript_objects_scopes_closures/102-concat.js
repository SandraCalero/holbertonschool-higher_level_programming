#!/usr/bin/node

const fs = require("fs");
const process = require("process");
const sourceFile1 = fs.readFileSync(process.argv[2], "utf8");
const sourceFile2 = fs.readFileSync(process.argv[3], "utf8");
const destFile = process.argv[4];

fs.appendFileSync(destFile, sourceFile1 + "\n" + sourceFile2 + "\n", "utf8");
