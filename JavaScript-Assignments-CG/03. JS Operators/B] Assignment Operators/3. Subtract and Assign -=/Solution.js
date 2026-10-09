// 1. Health is 100. Player takes 35 damage.
let health = 100;
health -= 35;

console.log(health); // 65
// Explanation: health = health - 35 = 100 - 35 = 65


// 2. Stock of 300 items is reduced by 45 after a sale.
let stock = 300;
stock -= 45;

console.log(stock); // 255


// 3. Predict the output.
let lives = 5;
lives -= 2;

console.log(lives); // 3
// Explanation: lives = 5 - 2 = 3


// 4. Predict the output.
let num = "40";
num -= 15;

console.log(num); // 25
// Explanation: The -= operator converts the numeric string "40"
// into the number 40 before subtraction.
// 40 - 15 = 25


// 5. Find the result and explain.
let x = "abc";
x -= 5;

console.log(x);        // NaN
console.log(typeof x); // number
// Explanation: "abc" cannot be converted into a valid number.
// Therefore, the subtraction produces NaN (Not-a-Number).
// NaN has the data type "number" in JavaScript.
