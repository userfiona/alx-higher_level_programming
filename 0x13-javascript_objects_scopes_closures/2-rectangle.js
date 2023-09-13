#!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If w or h is not a positive integer, set width and height to undefined
      this.width = undefined;
      this.height = undefined;
    }
  }
};
