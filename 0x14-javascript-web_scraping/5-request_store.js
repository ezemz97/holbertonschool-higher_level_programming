#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Requests the contents of a webpage and stores it in a UTF-8 encoded file.
// @param {string} url: Webpage to request.
// @param {string} path: File's full path to save.
const url = process.argv[2]
const path = process.argv[3]

request(url, function (_err, _res, body) {
  fs.writeFile(path, body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
