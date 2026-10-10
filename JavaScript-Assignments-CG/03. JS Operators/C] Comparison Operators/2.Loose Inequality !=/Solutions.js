// 1. Check whether "18" != 18 returns true or false.
console.log("18" != 18); // false
// Explanation: The string "18" is converted to the number 18.
// Both values are equal, so the result is false.


// 2. A password is stored as "1234".
// User enters 1234 (number). Will != return true?
let storedPassword = "1234";
let enteredPassword = 1234;

console.log(storedPassword != enteredPassword); // false
// Explanation: The string "1234" is converted to the number 1234.
// Both values are equal, so the result is false.


// 3. Predict the output.
console.log(5 != "5");  // false
console.log(0 != false); // false
// Explanation:
// "5" is converted to 5, so 5 != 5 is false.
// false is converted to 0, so 0 != 0 is false.


// 4. Predict the output.
console.log(null != undefined); // false
console.log("" != 0);           // false
// Explanation:
// null and undefined are loosely equal.
// The empty string "" is converted to 0.
// Both comparisons return false.


// 5. What does NaN != NaN return?
console.log(NaN != NaN); // true
// Explanation: NaN is not equal to any value, including itself.
// Therefore, NaN == NaN returns false, and NaN != NaN returns true.
