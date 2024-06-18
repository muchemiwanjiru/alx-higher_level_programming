#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occur = 0;
  for (const elmt in list) {
    if (list[elmt] === searchElement) occur++;
  }
  return occur;
};
