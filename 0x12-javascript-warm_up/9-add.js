#!/usr/bin/node

// Script that prints the addition of 2 integers

function add (a, b) {
  return a + b;
}

const a = parseInt(process.argv[2], 10);
const b = parseInt(process.argv[3], 10);

console.log(add(a, b));
