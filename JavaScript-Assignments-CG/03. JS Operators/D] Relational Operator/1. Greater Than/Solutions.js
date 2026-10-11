// 1. A student's marks are 78. The passing marks are 40.
// Check whether the student scored more than the passing marks.
let marks = 78;
let passingMarks = 40;

console.log(marks > passingMarks); // true
// Explanation: 78 is greater than 40.


// 2. Temperature today is 35°C and yesterday it was 28°C.
// Check if today is hotter.
let todayTemperature = 35;
let yesterdayTemperature = 28;

console.log(todayTemperature > yesterdayTemperature); // true
// Explanation: 35 > 28, so today is hotter.


// 3. Predict the output.
console.log(15 > 10); // true
console.log(10 > 15); // false
console.log(10 > 10); // false
// Explanation:
// 15 is greater than 10.
// 10 is not greater than 15.
// Equal values do not satisfy the > operator.


// 4. Predict the output.
console.log("20" > 15);    // true
console.log("5" > "10");   // true
console.log("abc" > 10);  // false

// Explanation:
// "20" > 15: The string "20" is converted to the number 20.
// 20 > 15 is true.

// "5" > "10": Both operands are strings, so JavaScript
// compares them lexicographically (character by character).
// "5" comes after "1", so the result is true.

// "abc" > 10: JavaScript attempts to convert "abc" into a number.
// The conversion produces NaN, so the comparison returns false.


// 5. Find the result of null > 0 and undefined > 0.
console.log(null > 0);      // false
console.log(undefined > 0); // false

// Explanation:
// null is converted to 0 during relational comparison.
// Therefore, 0 > 0 is false.

// undefined is converted to NaN.
// Comparisons involving NaN using > return false.


// 6. A shop has 120 items in stock.
// A customer wants to buy 85 items.
// Check whether stock is sufficient using >.
let stock = 120;
let requiredItems = 85;

console.log(stock > requiredItems); // true
// Explanation: 120 > 85, so the shop has sufficient stock.
// Note: >= would also allow purchases when stock exactly
// matches the required quantity.


// 7. Predict and explain the outputs.
console.log(true > false); // true
// Explanation: true converts to 1 and false converts to 0.
// Therefore, 1 > 0 is true.


console.log("10" > "2"); // false
// Explanation: Both values are strings.
// JavaScript compares their characters lexicographically.
// "1" comes before "2", so the result is false.


console.log(NaN > 5); // false
// Explanation: NaN represents Not-a-Number.
// Relational comparisons involving NaN always return false.
