#!/usr/bin/node
// prints factorial
function factorial (n) {
  if (n === 1) {
    return n;
  } else {
    return n * factorial(n - 1);
  }
}
if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  console.log(factorial(parseInt(process.argv[2])));
}
