#!/usr/bin/node
const fs = require('fs');

function concatenateFiles() {
  fs.readFile(process.argv[2], 'utf8', (err, first) => {
    if (err) {
      console.error('Error reading the first file:', err);
      return;
    }
    
    fs.readFile(process.argv[3], 'utf8', (err, second) => {
      if (err) {
        console.error('Error reading the second file:', err);
        return;
      }

      const combined = first + second;

      fs.writeFile(process.argv[4], combined, (err) => {
        if (err) {
          console.error('Error writing to the destination file:', err);
          return;
        }
        
        console.log('Files concatenated successfully.');
      });
    });
  });
}

concatenateFiles();
