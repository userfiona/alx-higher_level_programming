#!/usr/bin/node

// myFunction.js
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
