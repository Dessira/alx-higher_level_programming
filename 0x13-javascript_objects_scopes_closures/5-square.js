#!/usr/bin/node

// Class Square that defines a square and inherits from Rectangle
const Rectangle = require('./4-rectangle.js');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};