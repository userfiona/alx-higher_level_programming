#!/usr/bin/node

if (process.argv.length !== 4) {
  console.error('Error: Please provide exactly 2 arguments.');
  console.log('Usage: ./script.js arg1 arg2');
  process.exit(1); // Exit the script with an error code
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (!arg1 || !arg2) {
  console.error('Error: Both arguments must be non-empty.');
  console.log('Usage: ./script.js arg1 arg2');
  process.exit(1); // Exit the script with an error code
}

console.log(`${arg1} is ${arg2}`);
