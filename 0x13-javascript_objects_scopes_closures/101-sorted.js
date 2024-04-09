#!/usr/bin/node

const { dict } = require('./101-data.js');

const newDict = Object.keys(dict).reduce((acc, key) => {
  const occurrence = dict[key];
  if (!acc[occurrence]) {
    acc[occurrence] = [];
  }
  acc[occurrence].push(key);
  return acc;
}, {});

console.log(newDict);
