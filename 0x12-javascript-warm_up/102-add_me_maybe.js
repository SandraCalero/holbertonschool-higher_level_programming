#!/usr/bin/node
/// This function is incrementing and calls a function.
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
