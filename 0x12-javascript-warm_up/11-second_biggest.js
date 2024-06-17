#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
if (args.length < 2) {
  console.log(0);
} else {
  const max = Math.max(...args);
  const secondMax = args.filter(num => num < max).reduce((a, b) => Math.max(a, b), -Infinity);
  console.log(secondMax !== -Infinity ? secondMax : 0);
}
