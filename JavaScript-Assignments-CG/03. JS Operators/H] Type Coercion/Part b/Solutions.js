// JavaScript Practice – Type Conversion
// Questions 6–10


// 6. Predict the output.
{
    console.log("10" - 5); // 5
    console.log("10" + 5); // 105
    console.log("10" * 2); // 20
    console.log("10" / 2); // 5

    // Explanation:
    // The -, *, and / operators convert numeric strings into numbers.
    // The + operator performs concatenation when one operand is a string.
    // Therefore, "10" + 5 produces the string "105".
}


// 7. Predict the output.
{
    console.log("5" - "2"); // 3
    console.log("5" + "2"); // 52
    console.log("5" * "2"); // 10
    console.log("5" / "2"); // 2.5

    // Explanation:
    // Subtraction, multiplication, and division convert both strings
    // into numbers before performing the calculation.
    // The + operator joins the two strings, producing "52".
}


// 8. Predict the output.
{
    console.log(Number("123"));       // 123
    console.log(Number("123abc"));    // NaN
    console.log(Number(true));        // 1
    console.log(Number(false));       // 0
    console.log(Number(null));        // 0
    console.log(Number(undefined));   // NaN

    // Explanation:
    // "123" is a valid numeric string, so it becomes 123.
    // "123abc" cannot be converted into a valid number.
    // true converts to 1, while false converts to 0.
    // null converts to 0.
    // undefined converts to NaN (Not-a-Number).
}


// 9. Predict the output.
{
    console.log(Boolean(0));    // false
    console.log(Boolean(""));   // false
    console.log(Boolean("0"));  // true
    console.log(Boolean([]));   // true
    console.log(Boolean({}));   // true
    console.log(Boolean(null)); // false

    // Explanation:
    // 0, empty string "", and null are falsy values.
    // "0" is a non-empty string, so it is truthy.
    // Empty arrays [] and empty objects {} are also truthy.
}


// 10. Predict the output.
{
    console.log(String(100));       // "100"
    console.log(String(true));      // "true"
    console.log(String(null));      // "null"
    console.log(String(undefined)); // "undefined"
    console.log(100 + ""); // "100"
}