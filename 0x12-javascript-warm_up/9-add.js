#!/usr/bin/node
function add (a, b) {
  if (!isNaN(a) && !isNaN(b)) {
    return parseInt(a) + parseInt(b);
  }
  return NaN;
}
console.log(add(process.argv[2], process.argv[3]));
