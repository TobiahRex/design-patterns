let Color = Object.freeze({
    red: 'red',
    green: 'green',
    blue: 'blue'
})

let Size = Object.freeze({
    small: 'small',
    medium: 'medium',
    large: 'large'
})

class Product {
    constructor(name, color, size) {
        this.name = name;
        this.color = color;
        this.size = size;
    }


}

class ProductFilter {
    constructor() {

    }

    static filterByColor(products, color) {
        return products.filter((product) => product.color == color);
    }

    // NOTE: This violates the Open-Closed principle
    static filterBySize(products, size) {
        return products.filter((product) => product.size === size);
    }

    // NOTE: This violates the Open-Closed principle
    static filterBySizeAndColor(products, size, color) {
        return products.filter((product) => product.size === size && product.color === color);
    }
}
/*
    Open-Closed Principle:
        "Objects are OPEN for extension & CLOSED for modification"

    We should design our classes to follow the Open-Closed principle.

    The answer to implementing this strategy is thru "Specifications/Interfaces"
*/

const apple = new Product('apple', Color.green, Size.small);
const tree = new Product('Tree', Color.green, Size.large);
const house = new Product('House', Color.blue, Size.large);

const products = [apple, tree, house];
// let greenProducts = ProductFilter.filterByColor(products, Color.green)
// console.log('green products: ', greenProducts);

class ColorSpecification {
    constructor(color) {
        this.color = color
    }

    isSatisfied(product) {
        return product.color === this.color;
    }
}

class SizeSpecification {
    constructor(size) {
        this.size = size
    }

    isSatisfied(product) {
        return product.size === this.size;
    }
}

class BetterFilter {
    static filter(products, spec) {
        return products.filter((product) => spec.isSatisfied(product))
    }
}

const greenSpec = new ColorSpecification(Color.green);
const smallSpec = new SizeSpecification(Size.small);

// let greenProducts = BetterFilter.filter(products, greenSpec);
// console.log('green products: ', greenProducts);

// let smallProducts = BetterFilter.filter(products, smallSpec);
// console.log('small products: ', smallProducts);

class AndSpecification {
    constructor(...specs) {
        this.specs = specs;
    }

    isSatisfied(product) {
        return this.specs.every((spec) => spec.isSatisfied(product));
    }
}
let greenSmallSpec = new AndSpecification(greenSpec, smallSpec);
let greenSmallProducts = BetterFilter.filter(products, greenSmallSpec);
console.log('green small products: ', greenSmallProducts);