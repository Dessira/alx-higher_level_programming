#!/usr/bin/node

// Class Rectangle that defines a rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let j;
    let newstr = '';
    while (i < this.height) {
      j = 0;
      while (j < this.width) {
        newstr += 'X';
        j++;
      }
      console.log(newstr);
      newstr = '';
      i++;
    }
  }

  rotate () {
    const holder = this.width;
    this.width = this.height;
    this.height = holder;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
