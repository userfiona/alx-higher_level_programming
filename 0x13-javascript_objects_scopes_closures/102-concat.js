#!/usr/bin/node

const fs = require('fs');
const [sourceFile1, sourceFile2, destinationFile] = process.argv.slice(2);

if (!sourceFile1 || !sourceFile2 || !destinationFile) {
  console.error('Usage: concat-files.js <source-file1> <source-file2> <destination-file>');
  process.exit(1);
}

try {
  const data1 = fs.readFileSync(sourceFile1, 'utf8');
  const data2 = fs.readFileSync(sourceFile2, 'utf8');
  const concatenatedData = data1 + data2;
  fs.writeFileSync(destinationFile, concatenatedData, 'utf8');
  console.log(`Files '${sourceFile1}' and '${sourceFile2}' successfully concatenated to '${destinationFile}'.`);
} catch (err) {
  console.error(`Error: ${err.message}`);
  process.exit(1);
}
