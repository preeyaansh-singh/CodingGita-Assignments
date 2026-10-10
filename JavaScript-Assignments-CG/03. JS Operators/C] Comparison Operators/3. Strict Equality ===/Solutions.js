// 1. Check whether "25" === 25 returns true or false.
console.log("25" === 25); // false
// Explanation: "25" is a string, while 25 is a number.
// The === operator checks both value and data type without
// performing type conversion.


// 2. Check if 0 === false and null === undefined.
console.log(0 === false);        // false
console.log(null === undefined); // false
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
console.log('[]' === false); // false
// Explanation:
// "" is a string, while 0 is a number.
// [] is an array (object), while false is a boolean.
// Their data types differ, so both comparisons return false.


// 5. Why is === preferred over == in most real-world code?

console.log("5" == 5);  // true
console.log("5" === 5); // false

// Explanation:
// == performs type conversion when necessary.
// === compares both value and type without type conversion.
// Therefore, === makes comparisons more predictable and
// helps prevent unexpected type-related bugs.
