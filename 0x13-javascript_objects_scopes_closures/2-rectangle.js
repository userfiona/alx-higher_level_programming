 #!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If w or h is not a positive integer, create an empty object
      Object.defineProperty(this, 'width', { value: undefined, writable: true });
      Object.defineProperty(this, 'height', { value: undefined, writable: true });
    }
  }
};
