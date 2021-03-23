#!/usr/bin/node
let i = 0;
let biggest = parseInt(process.argv[2]), second;
for (i = 3; i < process.argv.length; i++) {
  if (parseInt(process.argv[i]) > biggest) {
    second = biggest;
    biggest = parseInt(process.argv[i]);
  }
}
console.log(second);
