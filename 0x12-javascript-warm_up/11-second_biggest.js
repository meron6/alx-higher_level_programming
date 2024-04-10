#!/usr/bin/node
const listArgs = process.argv;
if (listArgs.length <= 3) {
  console.log(0);
} else {
  listArgs.sort(function (a, b) {
    return a - b;
  });
  console.log(listArgs[listArgs.length - 2]);
}
