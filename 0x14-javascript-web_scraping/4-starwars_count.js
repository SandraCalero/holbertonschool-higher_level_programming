#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const endpoint = process.argv[2];

request(endpoint, function (error, body) {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body.body);
    const results = movies.results;
    const WedgeAntillesID = '18';
    let numberOfMovies = 0;
    for (const film in results) {
      const characters = results[film].characters;
      for (const characterID in characters) {
        if (characters[characterID].includes(WedgeAntillesID)) {
          numberOfMovies++;
        }
      }
    }
    console.log(numberOfMovies);
  }
});
