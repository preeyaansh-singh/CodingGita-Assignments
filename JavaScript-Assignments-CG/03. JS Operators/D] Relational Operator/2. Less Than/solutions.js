// 1. A box can hold a maximum of 50 kg.
// Current weight is 42 kg. Check if more items can be added.
let maxWeight = 50;
let currentWeight = 42;

console.log(currentWeight < maxWeight); // true
// Explanation: 42 < 50, so the box has remaining capacity.


// 2. A person's age is 16. Minimum required age is 18.
// Check whether the person is underage.
let age = 16;
let minimumAge = 18;

console.log(age < minimumAge); // true
// Explanation: 16 < 18, so the person is underage.


// 3. Predict the output.
console.log(8 < 12);  // true
console.log(20 < 10); // false
console.log(7 < 7);   // false

// Explanation:
// 8 is less than 12.
// 20 is not less than 10.
// Equal values do not satisfy the < operator.


// 4. Predict the output.
console.log("8" < 10);      // true
console.log("20" < "3");    // true
console.log("hello" < 5);  // false

// Explanation:
// "8" < 10: The string "8" is converted to the number 8.
// Therefore, 8 < 10 is true.

// "20" < "3": Both operands are strings, so JavaScript
// compares them lexicographically (character by character).
// "2" comes before "3", so the result is true.

// "hello" < 5: JavaScript attempts to convert "hello"
// into a number, which produces NaN.
// Comparisons involving NaN return false.


// 5. Find the result of null < 0 and undefined < 0.
console.log(null < 0);      // false
console.log(undefined < 0); // false

// Explanation:
// null is converted to 0 during relational comparison.
// Therefore, 0 < 0 is false.

// undefined is converted to NaN.
// Relational comparisons involving NaN return false.


// 6. A tank has a capacity of 500 litres.
// Current water level is 375 litres.
// Check whether the tank is not full using <.
let tankCapacity = 500;
let currentWaterLevel = 375;

console.log(currentWaterLevel < tankCapacity); // true
// Explanation: 375 < 500, so the tank is not full.


// 7. Predict and explain the outputs.

console.log(false < true); // true
// Explanation: false converts to 0 and true converts to 1.
// Therefore, 0 < 1 is true.


console.log("5" < "15"); // false
// Explanation: Both operands are strings.
// JavaScript compares their characters lexicographically.
// "5" comes after "1", so the result is false.


console.log(NaN < 10); // false
// Explanation: NaN represents Not-a-Number.
// Relational comparisons involving NaN always return false.