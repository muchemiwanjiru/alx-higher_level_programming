#!/usr/bin/node

const list = require('./100-data.js').list;
const newList = list.map(myFunction);

console.log(list);
console.log(newList);

function myFunction (number, index) { return number * index; }
