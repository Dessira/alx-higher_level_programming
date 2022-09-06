#!/usr/bin/node

// Script that prints x times a square
// Where x is the first argument of the script

const myArgs = process.argv.slice(2);
let i = 0;
let j;
const value = parseInt(myArgs, 10);
let holder;
let newstr = '';
if (myArgs === 'undefined') {
  console.log('Missing size');
} else if (value) {
  if (value > 0) {
    holder = value;
    while (i < holder) {
      j = 0;
      while (j < holder) {
        newstr += 'X';
        j++;
      }
      console.log(newstr);
      newstr = '';
      i++;
    }
  }
} else {
  console.log('Missing size');
}
