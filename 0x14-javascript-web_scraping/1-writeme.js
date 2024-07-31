#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length < 4) {
  console.error('Usage: ./1-writeme.js <file_path> <string_to_write>');
  process.exit(1);
}

// Get the file path and the string to write from the command-line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file in UTF-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf8', function (err) {
  if (err) {
    console.log(err);
  } else {
    console.log('File written successfully');
  }
});
