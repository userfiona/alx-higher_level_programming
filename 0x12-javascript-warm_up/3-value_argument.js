#!/usr/bin/node
const myArg = process.argv[2];
console.log(myArg === undefined ? 'No argument' : myArg);
