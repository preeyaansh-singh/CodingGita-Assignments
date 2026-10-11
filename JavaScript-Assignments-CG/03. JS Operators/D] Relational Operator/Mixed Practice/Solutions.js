// 1. Write expressions to check the following conditions.

// Check whether age 18 is greater than or equal to voting age 18.
let age = 18;
let votingAge = 18;

console.log(age >= votingAge); // true
// Explanation: 18 >= 18 is true.


// Check whether temperature 32 is less than 35.
let temperature = 32;

console.log(temperature < 35); // true
// Explanation: 32 is less than 35.


// Check whether score 90 is greater than 85.
let score = 90;

console.log(score > 85); // true
// Explanation: 90 is greater than 85.


// 2. Predict the outputs.

console.log(10 > 5 && 5 < 10); // true
// Explanation: Both conditions are true.
// true && true = true.


console.log("10" >= 10); // true
// Explanation: The string "10" is converted to the number 10.
// Therefore, 10 >= 10 is true.


console.log(null <= undefined); // false
// Explanation: null converts to 0 and undefined converts to NaN.
// Relational comparisons involving NaN return false.


console.log("5" < "10" && 5 > 2); // false
// Explanation: Both "5" and "10" are strings, so JavaScript
// compares them lexicographically.
// "5" < "10" is false because "5" comes after "1".
// 5 > 2 is true.
// false && true = false.


// 3. A product costs ₹499. A customer has ₹500.
// Check if the customer can buy it and if any change will be left.
let productPrice = 499;
let customerMoney = 500;

console.log(customerMoney >= productPrice); // true
// Explanation: 500 >= 499, so the customer can buy the product.

console.log(productPrice < customerMoney); // true
// Explanation: 499 < 500, so some money will be left.

console.log(customerMoney - productPrice); // 1
// The customer will receive ₹1 as change.


// 4. Explain why "10" > "2" is false but 10 > 2 is true.

console.log("10" > "2"); // false
// Explanation: Both operands are strings.
// JavaScript compares them lexicographically (character by character).
// "1" comes before "2", so "10" > "2" is false.


console.log(10 > 2); // true
// Explanation: Both operands are numbers.
// JavaScript performs a numerical comparison.
// Since 10 is greater than 2, the result is true.
