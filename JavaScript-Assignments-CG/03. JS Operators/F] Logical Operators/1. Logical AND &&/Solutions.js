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

// JavaScript Practice – Logical AND Operator (&&)
// Additional Questions (Q6 – Q10)


// 6. Predict the output.
{
    let a = 0;
    let b = 10;
    let result = a && b;

    console.log(result); // 0

    // Explanation:
    // 0 is a falsy value.
    // && returns the first falsy operand without evaluating further.
    // Therefore, the result is 0.
}


// 7. Predict the output.
{
    let x = 5;
    let y = 10;
    let result = (x > 3 && y) || 0;

    console.log(result); // 10

    // Explanation:
    // x > 3 returns true.
    // true && 10 returns 10.
    // 10 || 0 returns 10 because 10 is truthy.
}


// 8. Predict the output.
{
    let p = "Hello";
    let q = "";
    let r = "World";
    let result = p && q && r;

    console.log(result); // "" (Empty String)

    // Explanation:
    // "Hello" is truthy.
    // "" is falsy.
    // && stops at the first falsy operand and returns it.
    // Therefore, the result is an empty string.
}


// 9. Predict the output.
{
    let val = 5;
    let condition = val && (val = 0);

    console.log(condition); // 0
    console.log(val);       // 0

    // Explanation:
    // Initially, val = 5, which is truthy.
    // Therefore, the second operand (val = 0) is evaluated.
    // val becomes 0.
    // The assignment expression also returns 0.
    // Therefore, condition = 0 and val = 0.
}


// 10. Predict the output.
{
    let x = 10;
    let y = 20;
    let result = (x && y) && (x > y);

    console.log(result); // false

    // Explanation:
    // x && y returns 20 because both values are truthy.
    // x > y means 10 > 20, which is false.
    // Therefore, 20 && false returns false.
}