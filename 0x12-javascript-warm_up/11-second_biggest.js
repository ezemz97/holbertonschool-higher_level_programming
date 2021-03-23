#!/usr/bin/node
const argLen = (process.argv.length) - 2;
if (argLen === 0 || argLen === 1) {
  console.log(0);
} else {
  const prev = process.argv;
  prev.sort(function (a, b) { return a - b; });
  console.log(prev[prev.length - 2]);
}

/* My code
let i = 0;
let biggest = parseInt(process.argv[2]); let second = parseInt(process.argv[2]);

if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (i = 3; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > biggest) {
      second = biggest;
      biggest = parseInt(process.argv[i]);
    }
  }
  console.log(second);
}
*/
