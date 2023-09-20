#!/usr/bin/node

const numArgs = process.argv.length - 2;
const message = numArgs === 0 ? 'No argument' : numArgs === 1 ? 'Argument found' : 'Arguments found';

console.log(message);
