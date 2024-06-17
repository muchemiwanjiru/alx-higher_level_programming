#!/usr/bin/node
const num = parseInt(process.argv[2]);
console.log(Number.isInteger(num) ? `My number: ${num}` : 'Not a number');
