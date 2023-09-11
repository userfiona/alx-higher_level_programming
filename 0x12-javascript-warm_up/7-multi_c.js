#!/usr/bin/node

const x = Math.floor(Number(process.argv[2]));

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  const output = Array(x).fill('C is fun').join('\n');
  console.log(output);
}
