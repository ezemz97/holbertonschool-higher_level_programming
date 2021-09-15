#!/usr/bin/node
const fs = require('fs');

// Reads a file using the 'fs' (filesystem) module.
// @param {string} path: File's full path.
// @param {string} string: String to write to file.
const path = process.argv[2];
const string = process.argv[3];

fs.writeFile(path, string, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
