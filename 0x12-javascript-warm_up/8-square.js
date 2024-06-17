#!/usr/bin/node
const num = parseInt(process.argv[2]);

if (Number.isNaN(num)) {
  console.log('Missing size');
} else {
  const str = 'X'.repeat(num);
  for (let x = 0; x < num; x++) {
    console.log(str);
  }
}
