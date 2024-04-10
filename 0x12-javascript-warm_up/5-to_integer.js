#!/usr/bin/node
const convToInt = parseInt(process.argv[2]);
if (!convToInt || isNaN(convToInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convToInt);
}
