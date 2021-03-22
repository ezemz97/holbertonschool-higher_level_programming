#!/usr/bin/node

// Prints the first argument passed from the console
if (process.argv[2] != null) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
