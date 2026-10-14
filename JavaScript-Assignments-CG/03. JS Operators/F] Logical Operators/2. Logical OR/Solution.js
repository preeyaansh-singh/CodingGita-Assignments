// JavaScript Practice – Logical OR Operator (||)


// 1. A user can login with either a correct password or a valid OTP.
// Check if login is allowed using ||.
let passwordCorrect = true;
let otpValid = false;

console.log(passwordCorrect || otpValid); // true
// Explanation: true || false = true.
// At least one condition is true, so login is allowed.


// 2. A discount applies if the user is a member or has a coupon.
let isMember = false;
let hasCoupon = true;

console.log(isMember || hasCoupon); // true
// Explanation: false || true = true.
// The user has a coupon, so the discount applies.


// 3. Entry is allowed if age > 18 or height > 150 cm.
let age = 16;
let height = 155;

console.log(age > 18 || height > 150); // true
// Explanation: 16 > 18 is false, but 155 > 150 is true.
// false || true = true, so entry is allowed.


// 4. A form is valid if either email or phone is given.
let emailGiven = true;
let phoneGiven = false;

console.log(emailGiven || phoneGiven); // true
// Explanation: true || false = true.
// Email is provided, so the form is valid.


// 5. A game level opens if score > 1000 or time bonus is collected.
let score = 900;
let timeBonus = true;

console.log(score > 1000 || timeBonus); // true
// Explanation: 900 > 1000 is false, but timeBonus is true.
// false || true = true, so the game level opens.

// JavaScript Practice – Logical OR Operator (||)
// Additional Questions (Q6 – Q10)


// 6. Predict the output.
{
    let a = 0;
    let b = false;
    let c = "";
    let d = null;
    let e = 42;

    let result = a || b || c || d || e;

    console.log(result); // 42

    // Explanation:
    // 0, false, "", and null are all falsy values.
    // The || operator returns the first truthy operand.
    // Since 42 is truthy, the result is 42.
}


// 7. Predict the output.
{
    let x = "Hello" || 0;
    let y = 0 || "Hi";

    console.log(x, y); // Hello Hi

    // Explanation:
    // "Hello" is truthy, so x becomes "Hello".
    // 0 is falsy, so || evaluates and returns "Hi".
    // Therefore, x = "Hello" and y = "Hi".
}


// 8. Predict the output.
{
    let a = 10;
    let b = 20;
    let result = (a < 5) || (b > 15);

    console.log(result); // true

    // Explanation:
    // a < 5 means 10 < 5, which is false.
    // b > 15 means 20 > 15, which is true.
    // false || true = true.
}


// 9. Predict the output.
{
    let val = 5;
    let condition = val || (val = 0);

    console.log(condition); // 5
    console.log(val);       // 5

    // Explanation:
    // Initially, val = 5, which is truthy.
    // The || operator returns the first truthy operand.
    // Therefore, (val = 0) is never executed.
    // Both condition and val remain 5.
}


// 10. Predict the output.
{
    let x = "" || 0 || false || null || undefined || "OK";

    console.log(x); // OK

    // Explanation:
    // "", 0, false, null, and undefined are falsy values.
    // "OK" is the first truthy operand.
    // Therefore, || returns "OK".
}
