#!/usr/bin/node

function factorial(n) {
  if (n < 0 || isNaN(n)) {
    return "Factorial is not defined for NaN or negative numbers";
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const n = parseInt(process.argv[2]);
console.log(factorial(n));
