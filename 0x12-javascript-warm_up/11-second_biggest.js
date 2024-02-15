#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const arr = process.argv.sort().reverse();
  console.log(arr[1]);
}

