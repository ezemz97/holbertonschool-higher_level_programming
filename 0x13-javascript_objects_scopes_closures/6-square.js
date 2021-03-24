#!/usr/bin/node
const Squaremain = require('./5-square');

module.exports = class Square extends Squaremain {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.height));
    }
  }
};
