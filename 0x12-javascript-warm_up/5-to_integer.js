#!/usr/bin/node

// Script that prints My number: <first argument converted in integer>
// If the argument can’t be converted to an integer, print “Not a number”

const myArgs = process.argv.slice(2);
const value = parseInt(myArgs, 10);
if (myArgs === 'undefined') {
  console.log('Not a number');
} else if (value) {
  console.log('My number: ' + value);
} else {
  console.log('Not a number');
}
