#!/usr/bin/node
function factorial (number) {
  if (isNaN(number) || number === 0) {
    return (1);
  }
  return number * factorial(number - 1);
}
console.log(factorial(process.argv[2]));
