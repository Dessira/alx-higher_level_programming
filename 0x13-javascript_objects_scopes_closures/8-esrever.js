#!/usr/bin/node

// Function that returns the reversed version of a list

exports.esrever = function (list) {
  let len = list.length - 1;
  let newlist = [];
  while (len >= 0) {
    newlist = newlist.concat(list[len]);
    len--;
  }
  return newlist;
};
