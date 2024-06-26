#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    return;
  }
  fs.writeFile(filePath, body, 'utf8', function (err) {
    if (err) {
      console.error('error:', err);
    }
  });
});
