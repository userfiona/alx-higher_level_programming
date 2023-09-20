#!/usr/bin/node

class Rectangle {
  constructor(width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  /**
   * @property {method} print - prints the rectangle using the character X
   * @returns void
   */
  print() {
    if (!this.width || !this.height) return;

    const row = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }

  /**
   * @property {method} rotate - exchanges the width and the height of the rectangle
   * @returns void
   */
  rotate() {
    [this.width, this.height] = [this.height, this.width];
  }

  /**
   * @property {method} double - multiplies the width and the height of the rectangle by 2
   * @returns void
   */
  double() {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
