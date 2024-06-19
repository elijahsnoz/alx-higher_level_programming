#!/usr/bin/node

function add(a, b) {
  return a + b;
}

// Check if exactly two arguments are provided
if (process.argv.length !== 4) {
  console.log("Usage: ./9-add.js <first integer> <second integer>");
  process.exit(1); // Exit with error status
}

// Parse integers from command-line arguments and compute their sum
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

// Check if arguments are valid integers
if (isNaN(num1) || isNaN(num2)) {
  console.log("Please provide valid integers");
  process.exit(1); // Exit with error status
}

const result = add(num1, num2);
console.log(result);
