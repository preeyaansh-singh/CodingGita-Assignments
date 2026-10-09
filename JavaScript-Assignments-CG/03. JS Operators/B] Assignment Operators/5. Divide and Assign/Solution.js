// 1. A total of 180 chocolates is shared among 6 children.
let chocolates = 180;
chocolates /= 6;

console.log(chocolates); // 30
// Explanation: chocolates = 180 / 6 = 30


// 2. A distance of 300 km is covered in 5 hours.
// Find the average speed using /=.
let speed = 300;
speed /= 5;

console.log(speed); // 60
// Explanation: Average speed = 300 / 5 = 60 km/h


// 3. Predict the output.
let total = 400;
total /= 8;

console.log(total); // 50
// Explanation: total = 400 / 8 = 50


// 4. Predict the output.
let num = "100";
num /= 4;

console.log(num);        // 25
console.log(typeof num); // number
// Explanation: The /= operator converts the numeric string "100"
// into the number 100 before division.
// 100 / 4 = 25


// 5. Find the result and explain.
let z = 50;
z /= 0;

console.log(z); // Infinity
// Explanation: In JavaScript, a positive, non-zero number
// divided by positive zero produces Infinity.
// Therefore, 50 / 0 = Infinity.