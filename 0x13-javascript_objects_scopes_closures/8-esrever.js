#!/usr/bin/node

exports.esrever = function (list) {
  const revList = new Array(list.length);

  for (let i = list.length - 1, j = 0; i >= 0; --i, ++j) {
    revList[j] = list[i];
  }

  return revList;
};
