#!/usr/bin/node

// Prints two arguments passed to it, in the following format: “ is ”
let count = 0;
const myarg = process.argv.slice(2);
process.argv.forEach((val, index) => {
  count++;
});
if (count < 3) {
  console.log('undefined is undefined');
} else if (count === 3) {
  console.log(myarg[0] + ' is undefined');
} else {
  console.log(myarg[0] + ' is ' + myarg[1]);
}
