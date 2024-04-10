#!/usr/bin/node
// returns second biggest number
function sortNumbers (n) {
  const myArr = process.argv;
  myArr.shift();
  myArr.shift();

  const ordered = myArr.sort(function (a, b) {
    return a - b;
  });

  return parseInt(ordered[ordered.length - 2]);
}
if (process.argv[3]) {
  console.log(sortNumbers(process.argv));
} else {
  console.log(0);
}
