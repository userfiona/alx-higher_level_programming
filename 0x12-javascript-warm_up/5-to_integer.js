#!/usr/bin/node

const myArgs = process.argv.slice(2);
const firstArg = parseInt(myArgs[0]);

if (!isNaN(firstArg)) {
  console.log(`My number: ${firstArg}`);
} else {
  console.log('Not a number');
}
