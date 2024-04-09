#!/usr/bin/node
const args = process.argv.slice(2).map(Number).sort((a, b) => b - a);
let secondBiggest = 0;

if (args.length > 1) {
  secondBiggest = args[1];
  for (let i = 2; i < args.length; i++) {
    if (args[i] < secondBiggest) {
      secondBiggest = args[i];
      break;
    }
  }
}

console.log(secondBiggest);
