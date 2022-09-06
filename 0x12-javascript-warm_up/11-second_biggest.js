#!/usr/bin/node

// script that searches the second biggest integer in the list of arguments
const myArgs = process.argv.slice(2);
const size = myArgs.length;
if (size === 0 || size === 1) {
  console.log('0');
} else {
  let k = 0;
  let i = 0;
  let high = myArgs[0];
  while (k < 2) {
    while (i < size) {
      if (myArgs[i] > high) {
        high = myArgs[i];
      }
      i++;
    }
    if (k === 0) {
      const index = myArgs.indexOf(high);
      if (index > -1) {
        myArgs.splice(index, 1);
      }
    }
    i = 0;
    high = myArgs[0];
    k++;
  }
  console.log(high);
}
