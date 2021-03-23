#!/usr/bin/node
exports.add = function (a, b) {
  if (!isNaN(a) && !isNaN(b)) {
    return parseInt(a) + parseInt(b);
  }
  return NaN;
};
