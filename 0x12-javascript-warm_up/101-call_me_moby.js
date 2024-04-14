#!/usr/bin/node
// loop a function
const callMeMoby = function (n, func) {
  let i = 0;
  while (i < parseInt(n)) {
    func();
    i++;
  }
};
exports.callMeMoby = callMeMoby;
