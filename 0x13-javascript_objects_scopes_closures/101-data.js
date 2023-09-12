#!/usr/bin/node

const data = require('./101-data');

const occurrencesByUserId = data.dict;
const userIdsByOccurrence = {};

for (const userId in occurrencesByUserId) {
  const occurrence = occurrencesByUserId[userId];
  if (!userIdsByOccurrence[occurrence]) {
    userIdsByOccurrence[occurrence] = [];
  }
  userIdsByOccurrence[occurrence].push(Number(userId));
}

console.log(userIdsByOccurrence);
