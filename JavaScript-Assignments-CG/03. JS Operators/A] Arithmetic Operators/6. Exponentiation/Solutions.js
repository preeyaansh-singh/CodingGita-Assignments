
// 1. Find the volume of a cube with a side length of 6 cm.
let side = 6;
let volume = side ** 3;

console.log(volume); // 216
// Explanation: 6 ** 3 = 6 * 6 * 6 = 216 cm³


// 2. Find the total number of cells in a square arrangement
// with 9 cells on each side.
let cellsPerSide = 9;
let totalCells = cellsPerSide ** 2;

console.log(totalCells); // 81
// Explanation: 9 ** 2 = 9 * 9 = 81 cells


// 3. Calculate 5 raised to the power 4.
console.log(5 ** 4); // 625
// Explanation: 5 * 5 * 5 * 5 = 625


// 4. A square digital image has 1,024 pixels on each side.
// Find the total number of pixels.
let pixels = 1024;
let totalPixels = pixels ** 2;

console.log(totalPixels); // 1048576
// Explanation: 1024 ** 2 = 1,048,576 pixels


// 5. Predict the output.
let base = 2;
let power = -1;
let result = base ** power;

console.log(result); // 0.5
// Explanation: 2 ** -1 = 1 / 2 = 0.5


// 6. Find the output of 3 ** 4.
console.log(3 ** 4); // 81
// Explanation: 3 * 3 * 3 * 3 = 81


// 7. Calculate the area of a square with a side of 9 units.
let squareSide = 9;
let area = squareSide ** 2;

console.log(area); // 81
// Explanation: Area = side ** 2 = 9 * 9 = 81 square units


// 8. Compare 2 ** 5 and 5 ** 2.
console.log(2 ** 5); // 32
console.log(5 ** 2); // 25
// Explanation: They are not equal.
// 2 ** 5 = 32, whereas 5 ** 2 = 25.


// 9. Predict and explain the outputs.

// Exponentiation is right-associative.
console.log(2 ** 3 ** 2); // 512
// Explanation: 2 ** (3 ** 2) = 2 ** 9 = 512


console.log((2 ** 3) ** 2); // 64
// Explanation: (2 ** 3) ** 2 = 8 ** 2 = 64


console.log(2 ** -3); // 0.125
// Explanation: 2 ** -3 = 1 / (2 ** 3) = 1 / 8 = 0.125


// console.log(-2 ** 2);
// SyntaxError: Parentheses are required when a unary operator
// appears immediately before the base of **.


console.log((-2) ** 2); // 4
// Explanation: (-2) * (-2) = 4


console.log(4 ** 0.5); // 2
// Explanation: 4 ** 0.5 is equivalent to the square root of 4.


// 10. Predict the output.
let a = 10;
let b = 0;
let result2 = a ** b;

console.log(result2); // 1
// Explanation: Any non-zero number raised to the power 0 is 1.

