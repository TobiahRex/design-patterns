/*
    A class with a method should be able to take a base type(class/instance) as well as a derived type(class/instance).
*/
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }

    area() {
        return this.height * this.width
    }

    toString() {
        return `${this.width} x ${this.height}`;
    }
}

let rectangle = new Rectangle(2, 3)
console.log(rectangle.toString())