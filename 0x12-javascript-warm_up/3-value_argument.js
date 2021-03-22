#!/usr/bin/node

// Prints the first argument passed from the console
const arglen = process.argv.length;
if (arglen >= 3) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
