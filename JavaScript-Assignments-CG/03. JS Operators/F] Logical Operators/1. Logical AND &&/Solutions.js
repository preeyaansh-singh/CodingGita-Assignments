// JavaScript Practice – Logical AND Operator (&&)


// 1. Stored username is "admin" and password is 1234.
// Check if both are valid using &&.
let storedUsername = "admin";
let storedPassword = 1234;

let username = "admin";
let password = 1234;

console.log(username === storedUsername && password === storedPassword); // true
// Explanation: Both username and password match.
// true && true = true.


// 2. A user is logged in and has permission.
// Check if they can access a page using &&.
let isLoggedIn = true;
let hasPermission = true;

console.log(isLoggedIn && hasPermission); // true
// Explanation: Both conditions are true, so access is allowed.


// 3. A product is in stock and its price is less than ₹1000.
// Check if it can be bought using &&.
let inStock = true;
let price = 800;

console.log(inStock && price < 1000); // true
// Explanation: The product is available and 800 < 1000.
// Both conditions are true.


// 4. A student has marks 75 and attendance 80.
// Passing requires marks > 65 and attendance > 70.
let marks = 75;
let attendance = 80;

console.log(marks > 65 && attendance > 70); // true
// Explanation: 75 > 65 and 80 > 70.
// true && true = true, so the student passes.


// 5. A party happens only if it is both a weekend and a holiday.
let isWeekend = true;
let isHoliday = false;

console.log(isWeekend && isHoliday); // false
// Explanation: One condition is false.
// true && false = false, so the party does not happen.