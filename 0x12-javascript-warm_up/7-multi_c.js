#!/usr/bin/node

const numOccurrences = parseInt(process.argv[2]);

if (!isNaN(numOccurrences) && numOccurrences > 0) {
  let output = '';
  for (let i = 0; i < numOccurrences; i++) {
    output += 'C is fun\n';
  }
  console.log(output.trim()); // Print the accumulated output with line breaks trimmed
} else {
  console.log('Missing number of occurrences');
}
