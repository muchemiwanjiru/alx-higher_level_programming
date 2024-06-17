#!/usr/bin/node
// script that prints a message depending of the number of arguments passed
const myVar = process.argv.length;
console.log(myVar === 2 ? 'No argument' : myVar === 3 ? 'Argument found' : 'Arguments found');
