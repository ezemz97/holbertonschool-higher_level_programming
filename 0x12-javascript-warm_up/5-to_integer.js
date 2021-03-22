#!/usr/bin/node
const numero = parseInt(process.argv[2]);
if (isNaN(numero)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + numero);
}
