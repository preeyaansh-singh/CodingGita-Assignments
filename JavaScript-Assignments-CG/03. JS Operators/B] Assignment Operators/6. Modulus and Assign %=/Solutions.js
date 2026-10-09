// 1. Number 47 is divided by 6.
// Store only the remainder using %=.
let number = 47;
number %= 6;

console.log(number); // 5
// Explanation: number = 47 % 6 = 5


// 2. Counter is at 23.
// Keep only the remainder when divided by 12.
let counter = 23;
counter %= 12;

console.log(counter); // 11
// Explanation: counter = 23 % 12 = 11


// 3. Predict the output.
let num = 29;
num %= 5;

console.log(num); // 4
// Explanation: num = 29 % 5 = 4


// 4. Predict the output.
let x = "17";
x %= 3;

console.log(x);        // 2
console.log(typeof x); // number
// Explanation: The %= operator converts the numeric string "17"
// into the number 17 before calculating the remainder.
// 17 % 3 = 2


// 5. Find the result and explain.
let m = 15;
m %= 0;

console.log(m); // NaN
// Explanation: The remainder operation with a divisor of zero
// produces NaN (Not-a-Number) in JavaScript.

