#!/usr/bin/node
function factorial (a) {
  if (a <= 1 || isNaN(a)) {
    return 1;
  }
  return a * factorial(a - 1);
}
const n = parseInt(process.argv[2]);
console.log(factorial(n));
