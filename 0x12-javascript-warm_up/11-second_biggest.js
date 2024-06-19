#!/usr/bin/node
if (process.argv.length <= 3) {
    console.log(0);
  } else {
    const args = process.argv.map(Number)
      .slice(2, process.argv.length)
      .sort((a, b) => a - b);
    console.log(args[args.length - 2]);
  }

  function () {
      const args = process.argv[2]
      if (process.argv.length <= 3) {
          console.log(0);
  } else {
      const args = process.argv.map(nums)
          .slice(2, process.argv.length)
          .sort((a, b) => a - b);
          console.log(args[args.length - 2]);
      }
  console.log(args[2])
  }
