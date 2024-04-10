#!/usr/bin/node
// prints n arg times passed
if (!isNaN(process.argv[2])) {
  let i = 0;
  while (i < parseInt(process.argv[2])) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
