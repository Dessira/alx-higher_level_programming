#!/usr/bin/node

// Class Square that defines a square and inherits from Rectangle
const Rectangle = require('./4-rectangle.js');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c) {
      let i = 0;
      let j;
      while (i < this.size) {
        let newstr = '';
        j = 0;
        while (j < this.size) {
          newstr += 'C';
          j++;
        }
        console.log(newstr);
        i++;
      }
    } else {
      this.print();
    }
  }
};
