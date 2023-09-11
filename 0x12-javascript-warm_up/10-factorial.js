#!/usr/bin/node

function factorial(num) {
  if (isNaN(num) || num < 0) {
    return "Factorial is not defined for NaN or negative numbers";
  } else if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const inputNumber = parseInt(process.argv[2]);

console.log(`Factorial of ${isNaN(inputNumber) ? 'NaN' : inputNumber} is ${factorial(inputNumber)}`);
