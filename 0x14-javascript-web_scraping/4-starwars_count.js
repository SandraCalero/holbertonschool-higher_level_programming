#!/usr/bin/node
// This script is printing the number of movies
// where the character “Wedge Antilles” is present.
const request = require('request');
const endpoint = process.argv[2];

request(endpoint, function (error, body) {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body.body);
    const results = movies.results;
    const WedgeAntillesUrl = 'https://swapi-api.hbtn.io/api/people/18/';
    let numberOfMovies = 0;
    let item;
    for (item of results) {
      if (item.characters.includes(WedgeAntillesUrl)) {
        numberOfMovies++;
      }
    }
    console.log(numberOfMovies);
  }
});
