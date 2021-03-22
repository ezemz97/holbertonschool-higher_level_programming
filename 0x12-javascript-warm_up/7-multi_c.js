#!/usr/bin/node
const numero = parseInt(process.argv[2]);
let i = 0;
if (isNaN(numero)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < numero; i++) {
    console.log('C is fun');
  }
}
