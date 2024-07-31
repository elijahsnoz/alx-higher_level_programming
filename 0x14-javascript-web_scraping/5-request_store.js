#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length < 4) {
  console.error('Usage: ./5-request_store.js <URL> <file_path>');
  process.exit(1);
}

// Get the URL and file path from the command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make the GET request to the URL
request(url, function (err, res, body) {
  if (err) {
    console.error('Error fetching URL:', err);
    process.exit(1);
  }

  // Write the response body to the specified file in UTF-8 encoding
  fs.writeFile(filePath, body, 'utf8', function (writeErr) {
    if (writeErr) {
      console.error('Error writing file:', writeErr);
      process.exit(1);
    }
    console.log('File saved successfully');
  });
});
