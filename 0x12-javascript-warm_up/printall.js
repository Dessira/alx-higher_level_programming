#!/usr/bin/node

// script that prints the first argument passed to it
// If no arguments are passed to the script, print “No argument”

let num = 0;

process.argv.forEach((val, index) => {
  if (index > 1) {
    console.log(`${val}`);
    num = 0;
  } else {
    num = 3;
  }
});
if (num === 3) {
  console.log('No argument');
}
