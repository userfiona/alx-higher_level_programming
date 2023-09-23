#!/usr/bin/node

function add(a, b) { // Remove the space before '('
  return a + b;
}

const firstInteger = parseInt(process.argv[2]);
const secondInteger = parseInt(process.argv[3]);

console.log(add(firstInteger, secondInteger));
