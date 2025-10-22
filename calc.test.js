const test = require('node:test');
const assert = require('node:assert');

const Calc = require('./Calc');

test('Calc.add returns the sum of two integers', () => {
    assert.strictEqual(Calc.add(2, 3), 5);
});

test('Calc.subtract returns the difference of two integers', () => {
    assert.strictEqual(Calc.subtract(5, 2), 3);
});

test('Calc.multiply returns the product of two integers', () => {
    assert.strictEqual(Calc.multiply(4, 3), 12);
});

test('Calc.divide returns the quotient of two integers when divisible', () => {
    assert.strictEqual(Calc.divide(10, 2), 5);
});

test('Calc.divide returns floating point results for non-even division', () => {
    assert.strictEqual(Calc.divide(7, 2), 3.5);
});

test('Calc.divide throws when dividing by zero', () => {
    assert.throws(() => Calc.divide(4, 0), {
        name: 'Error',
        message: 'Cannot divide by zero',
    });
});
