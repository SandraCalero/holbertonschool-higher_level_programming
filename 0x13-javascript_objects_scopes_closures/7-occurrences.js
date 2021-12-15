#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let numOcurr = 0;
  for (const idx in list) {
    if (list[idx] === searchElement) {
      numOcurr++;
    }
  }
  return numOcurr;
};
