// 1. Check whether the string "25" is loosely equal to the number 25.
console.log("25" == 25); // true
// Explanation: The == operator converts the numeric string "25"
// into the number 25 before comparing them.


// 2. Check if 0 == false returns true or false.
console.log(0 == false); // true
// Explanation: During loose equality comparison, false is converted
// to 0. Therefore, 0 == 0 returns true.


// 3. Predict the output.
console.log(10 == "10");       // true
console.log(null == undefined); // true
// Explanation:
// 10 == "10": The string "10" is converted to the number 10.
// null == undefined: These two values are loosely equal
// according to JavaScript's special equality rules.


// 4. Predict the output.
console.log("" == 0);      // true
console.log([] == false); // true
// Explanation:
// "" == 0: The empty string is converted to the number 0.
// [] == false: The empty array is converted to an empty string "",
// and then "" is converted to 0. Therefore, 0 == 0 is true.


// 5. Why does NaN == NaN return false?
console.log(NaN == NaN); // false
// Explanation: NaN represents an invalid or unrepresentable
// numeric result. Under JavaScript equality rules, NaN is not
// equal to any value, including itself.
// Use Number.isNaN() to check whether a value is NaN.
console.log(Number.isNaN(NaN)); // true


//Key concept:** The loose equality operator (`==`) may convert values to compatible types before comparing them. The strict equality operator (`===`) does not perform this type conversion.
//For example:
console.log("25" == 25);  // true
console.log("25" === 25); // false
