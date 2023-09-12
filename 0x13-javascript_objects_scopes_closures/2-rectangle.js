#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = undefined; // or this.width = null;
      this.height = undefined; // or this.height = null;
    }
  }
};
