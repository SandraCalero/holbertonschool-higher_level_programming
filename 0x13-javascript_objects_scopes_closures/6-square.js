#!/usr/bin/node

const Square0 = require('./5-square.js');

module.exports = class Square extends Square0 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let row = 0; row < this.height; row++) {
      console.log(c.repeat(this.width));
    }
  }
};
