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
const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);
const result = add(num1, num2);

console.log(result);
