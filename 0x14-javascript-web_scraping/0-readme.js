#!/usr/bin/node

const fs = require('fs');

// Check if the file path argument is provided
if (process.argv.length < 3) {
  console.error('Usage: ./script.js <file_path>');
  process.exit(1);
}

// Get the file path from the command-line arguments
const filePath = process.argv[2];

// Read the file in UTF-8 encoding
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    process.exit(1);
  } else {
    process.stdout.write(data);
  }
});
