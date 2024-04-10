#!/usr/bin/node
// nested loops
if (!isNaN(process.argv[2])) {
  let i = 0;
  let j = 0;

  const size = parseInt(process.argv[2]);
  while (i < size) {
    let myStr = '';
    while (j < size) {
      myStr += 'X';
      j++;
    }
    console.log(myStr);
    i++;
    j = 0;
  }
} else {
  console.log('Missing size');
}
