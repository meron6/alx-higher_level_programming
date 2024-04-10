#!/usr/bin/node
// increments with a function
const addMeMaybe = function (n, func) {
  const nb = parseInt(n) + 1;
  func(nb);
};
exports.addMeMaybe = addMeMaybe;
