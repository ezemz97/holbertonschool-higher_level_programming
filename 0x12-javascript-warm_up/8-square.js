#!/usr/bin/node
// Prints a square represented by 'X' n times (n being the first argument passed to the script)
const numero = parseInt(process.argv[2]);
let x = 0; let y = 0;
let square = '';
if (isNaN(numero)) {
  console.log('Missing size');
} else if (numero > 0) {
  for (x = 0; x < numero; x++) {
    for (y = 0; y < numero; y++) {
      square += 'X';
    }
    if (x !== numero - 1) {
      square += '\n';
    }
  }
  console.log(square);
}
