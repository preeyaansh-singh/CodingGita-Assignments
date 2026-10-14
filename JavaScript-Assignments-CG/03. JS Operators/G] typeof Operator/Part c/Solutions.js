// JavaScript Practice – typeof Operator
// Additional Questions (Q11 – Q15)


// 11. Predict the output.
{
    console.log(typeof typeof 100);  // string
    console.log(typeof typeof "Hi"); // string
    console.log(typeof typeof true); // string

    // Explanation:
    // typeof 100 returns "number".
    // typeof "Hi" returns "string".
    // typeof true returns "boolean".
    // The typeof operator always returns a string.
    // Therefore, applying typeof again returns "string".
}


// 12. Predict the output.
{
    let a = 10;
    let b = "10";

    console.log(typeof a === typeof b); // false
    console.log(typeof a == typeof b);  // false

    // Explanation:
    // typeof a returns "number".
    // typeof b returns "string".
    // Both are different strings.
    // Therefore, both == and === return false.
}


// 13. Predict the output.
{
    console.log(typeof null === "object"); // true
    console.log(typeof [] === "object");   // true
    console.log(typeof {} === "object");   // true

    // Explanation:
    // typeof null returns "object" due to a historical JavaScript bug.
    // Arrays are classified as objects in JavaScript.
    // {} represents an object.
    // Therefore, all three comparisons return true.
}


// 14. Predict the output.
{
    let x;

    console.log(typeof x); // undefined

    x = null;
    console.log(typeof x); // object

    x = 0;
    console.log(typeof x); // number

    // Explanation:
    // Initially, x has no assigned value, so its type is "undefined".
    // After assigning null, typeof x returns "object".
    // After assigning 0, its type becomes "number".
    // JavaScript allows variables to hold values of different types.
}


// 15. Predict the output.
{
    console.log(typeof NaN === "number");      // true
    console.log(typeof Infinity === "number"); // true
    console.log(typeof (1 / 0));               // number

    // Explanation:
    // NaN has the data type "number" in JavaScript.
    // Infinity is also classified as a number.
    // 1 / 0 produces Infinity in JavaScript.
    // Therefore, typeof (1 / 0) returns "number".
}