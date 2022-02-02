#!/usr/bin/node
// Script that computes the number of tasks completed by user id
const request = require('request');
const requestUrl = process.argv[2];
request(requestUrl, function (error, body) {
  if (error) {
    console.log(error);
  } else {
    const tasksInfo = JSON.parse(body.body);
    const taskInfoFilter = tasksInfo.filter(function (task) {
      return task.completed;
    });
    const count = {};
    for (const task in taskInfoFilter) {
      const userID = taskInfoFilter[task].userId;
      if (count[userID]) {
        count[userID] += 1;
      } else {
        count[userID] = 1;
      }
    }
    console.log(count);
  }
});
