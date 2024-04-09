#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
if (args.length < 2) {
  console.log(0);
} else {
  const uniqueArgs = [...new Set(args)].sort((a, b) => a - b);
  console.log(uniqueArgs[uniqueArgs.length - 2]);
}
