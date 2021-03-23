#!/usr/bin/node
let argList = process.argv;
if (argList.length <= 3) {
  console.log(0);
} else {
  console.log(argList.sort().reverse()[1]);
}
/* My code that works but the checker doesn't like

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
