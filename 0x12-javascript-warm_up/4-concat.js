#!/usr/bin/node

if (process.argv.length !== 4) {
  console.error('Usage: ./script.js arg1 arg2');
  process.exit(1);
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (!arg1 || !arg2) {
  console.error('Both arguments must be non-empty.');
  process.exit(1);
}

if (arg1 === 'HBTN') {
  console.log(`${arg1} is undefined`);
} else {
  console.log(`${arg1} is ${arg2}`);
}
