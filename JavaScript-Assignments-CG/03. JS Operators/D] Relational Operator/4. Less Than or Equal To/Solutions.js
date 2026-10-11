// 1. Maximum speed limit is 60 km/h.
// A vehicle is travelling at 60 km/h. Check if it is within the limit.
let speedLimit = 60;
let vehicleSpeed = 60;

console.log(vehicleSpeed <= speedLimit); // true
// Explanation: 60 is equal to 60, so the vehicle is within the limit.


// 2. A student needs at least 40 marks to pass.
// He scored 39. Check if he has failed.
let marks = 39;
let passingMarks = 40;

console.log(marks <= passingMarks - 1); // true
// Explanation: 39 <= 39 is true, so the student has failed.
// For integer marks, this checks whether the score is below 40.
// The simpler condition for failure is marks < passingMarks.


// 3. Predict the output.
console.log(15 <= 20); // true
console.log(20 <= 15); // false
console.log(15 <= 15); // true

// Explanation:
// 15 is less than 20, so the result is true.
// 20 is greater than 15, so the result is false.
// 15 is equal to 15, so the result is true.


// 4. Predict the output.
console.log("15" <= 20);  // true
console.log("30" <= "5"); // true
console.log(null <= 0);   // true

// Explanation:
// "15" <= 20: The string "15" is converted to the number 15.
// Therefore, 15 <= 20 is true.

// "30" <= "5": Both operands are strings, so JavaScript
// compares them lexicographically (character by character).
// "3" comes before "5", so the result is true.

// null <= 0: null is converted to the number 0.
// Therefore, 0 <= 0 is true.


// 5. What is the result of undefined <= 0?
console.log(undefined <= 0); // false
// Explanation: undefined is converted to NaN during comparison.
// Relational comparisons involving NaN return false.


// 6. A bag can hold a maximum of 10 books.
// Currently, it has 10 books.
// Check if more books can be added using <=.
let bagCapacity = 10;
let currentBooks = 10;

console.log(currentBooks + 1 <= bagCapacity); // false
// Explanation: 10 + 1 <= 10 is false.
// Adding another book would exceed the bag's capacity.
// Therefore, no more books can be added.


// 7. Predict and explain the outputs.

console.log(false <= 0); // true
// Explanation: false is converted to the number 0.
// Therefore, 0 <= 0 is true.


console.log("" <= 0); // true
// Explanation: The empty string "" is converted to the number 0.
// Therefore, 0 <= 0 is true.


console.log(NaN <= 5); // false
// Explanation: NaN represents Not-a-Number.
// Relational comparisons involving NaN always return false.
