#!/usr/bin/node

function factorial(num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const inputNumber = parseInt(process.argv[2]);

console.log(`Factorial of ${isNaN(inputNumber) ? 'NaN' : inputNumber} is ${factorial(inputNumber)}`);
