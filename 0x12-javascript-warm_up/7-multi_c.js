#!/usr/bin/node
const num = parseInt(process.argv[2]);
const x = 'C is fun';

for (let j = 0; j < num; j++) {
  console.log(x);
}

if (Number.isNaN(num)) {
  console.log('Missing number of occurrences');
}
