#!/usr/bin/node
const request = require('request');

// Print the response status code using the 'request' module.
// @param {string} url
const url = process.argv[2];

request(url, function (_err, res) {
  console.log('code:', res.statusCode);
});
