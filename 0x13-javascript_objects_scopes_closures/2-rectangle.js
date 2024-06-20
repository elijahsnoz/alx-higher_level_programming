#!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }
};
