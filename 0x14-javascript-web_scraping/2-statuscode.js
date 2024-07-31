#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length < 3) {
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

// Get the URL from the command-line arguments
const url = process.argv[2];

// Make the GET request
request(url, function (err, res) {
  if (err) {
    console.error('Error:', err);
  } else {
    console.log('code:', res.statusCode); // Print the response status code if a response was received
  }
});
