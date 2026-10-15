// JavaScript Practice – Type Conversion
// Questions 1–5


// 1. Convert the string "25" into a number using Number()
// and add 10 to it.
let num = Number("25");

console.log(num + 10); // 35
// Explanation: Number("25") converts the string into the number 25.
// Therefore, 25 + 10 = 35.


// 2. Convert the number 100 into a string using String()
// and join it with " rupees".
let amount = String(100);

console.log(amount + " rupees"); // 100 rupees
// Explanation: String(100) converts the number into a string.
// The + operator joins both strings.


// 3. Convert the value 0 into a boolean using Boolean().
let value = Boolean(0);

console.log(value); // false
// Explanation: 0 is a falsy value in JavaScript.


// 4. Convert the value "Hello" into a boolean.
let message = Boolean("Hello");

console.log(message); // true
// Explanation: A non-empty string is a truthy value.


// 5. Use the unary + operator to convert "50" into a number
// and multiply it by 2.
let number = +"50";

console.log(number * 2); // 100
// Explanation: Unary + converts "50" into the number 50.
// Therefore, 50 * 2 = 100