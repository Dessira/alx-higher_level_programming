#!/usr/bin/node

// Script that prints x times “C is fun”
// Where x is the first argument of the script

const myArgs = process.argv.slice(2);
let i = 0;
const value = parseInt(myArgs, 10);
if (myArgs === 'undefined') {
  console.log('Missing number of occurrences');
} else if (value) {
  if (value > 0) {
    while (i < value) {
      console.log('C is fun');
      i++;
    }
  }
} else {
  console.log('Missing number of occurrences');
}
