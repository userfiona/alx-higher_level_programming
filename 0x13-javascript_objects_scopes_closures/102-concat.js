#!/usr/bin/node
const fs = require('fs').promises;

async function concatFiles() {
  try {
    const file1Data = await fs.readFile(process.argv[2], 'utf-8');
    const file2Data = await fs.readFile(process.argv[3], 'utf-8');
    const output = file1Data + file2Data;
    await fs.writeFile(process.argv[4], output);
    console.log('Files concatenated successfully.');
  } catch (err) {
    console.error('An error occurred:', err);
  }
}

concatFiles();
