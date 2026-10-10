// 1. Check whether "25" === 25 returns true or false.
// Explain why.
console.log("25" === 25); // false
// Explanation: The string "25" and the number 25 have different
// data types. The === operator checks both value and type
// without performing type conversion.


// 2. Check if 0 === false and null === undefined.
console.log(0 === false);          // false
console.log(null === undefined);   // false
// Explanation:
// 0 is a number, while false is a boolean.
// null and undefined are different values and types.


// 3. Predict the output.
console.log(10 === "10"); // false
console.log(true === 1);  // false
// Explanation:
// 10 is a number, while "10" is a string.
// true is a boolean, while 1 is a number.
// Strict equality does not convert their types.


// 4. Predict the output.
console.log("" === 0);      // false
console.log([] === false); // false
// Explanation:
// "" is a string, while 0 is a number.
// [] is an object (array), while false is a boolean.
// Their types differ, so both comparisons return false.


// 5. Why is === preferred over == in most real-world code?

// The === operator checks both value and data type.
// It avoids unexpected results caused by automatic type conversion.

console.log("5" == 5);  // true
console.log("5" === 5); // false

// Explanation:
// == performs type conversion when applicable.
// === compares without converting types.
// Therefore, === makes comparisons more predictable
// and helps prevent type-related bugs.
