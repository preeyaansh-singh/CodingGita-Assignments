// 1. Price of an item is ₹500. Apply 18% GST.
let price = 500;
price *= 1.18;
console.log(price); // 590
// Explanation: price = 500 * 1.18 = 590


// 2. A quantity of 8 is tripled.
let quantity = 8;
quantity *= 3;
console.log(quantity); // 24
// Explanation: quantity = 8 * 3 = 24


// 3. Predict the output.
let amount = 200;
amount *= 1.1;
console.log(amount); // 220.00000000000003 may occur in some calculations
// Explanation: amount = 200 * 1.1
// Mathematically, the result is 220.
// Note: JavaScript floating-point arithmetic can sometimes produce small precision differences.

// 4. Predict the output.
let val = "7";
val *= 3;
console.log(val);        // 21
console.log(typeof val); // number
// Explanation: The string "7" is converted into the number 7.
// 7 * 3 = 21


// 5. Find the result and explain.
let y = "hello";
y *= 2;
console.log(y);        // NaN
console.log(typeof y); // number
// Explanation: "hello" cannot be converted into a number.
// Therefore, multiplication produces NaN.
