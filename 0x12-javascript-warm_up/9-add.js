#!/usr/bin/node
// addition
function add (a, b) {
  if (!isNaN(a) && !isNaN(b)) {
    console.log(parseInt(a) + parseInt(b));
  } else {
    console.log('NaN');
  }
}
add(process.argv[2], process.argv[3]);
