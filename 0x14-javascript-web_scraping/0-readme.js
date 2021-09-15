#!/usr/bin/node
const fs = require('fs');

// Reads a file in UTF-8 using the 'fs' (filesystem) module.
// @param {string} path: File's full path.
const path = process.argv[2];

fs.readFile(path, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
