// JavaScript Practice – Type Conversion
// Questions 19–23


// 19. Predict the output.
{
    let count = 5;

    console.log(typeof count++); // number
    console.log(count);          // 6
    console.log(typeof ++count); // number
    console.log(count);          // 7

    // Explanation:
    // count++ (Post-increment) returns the old value, then increments it.
    // ++count (Pre-increment) increments the value first, then returns it.
    // Both operations return numbers.
}


// 20. Predict the output.
{
    let x = "10";
    let y = ++x;

    console.log(x, y, typeof x, typeof y);
    // Output: 11 11 number number

    // Explanation:
    // ++x converts the string "10" into a number.
    // It then increments 10 to 11.
    // Both x and y contain the number 11.
}


// 21. Predict the output.
{
    let a = "5";
    let b = a++;

    console.log(a, b, typeof a, typeof b);
    // Output: 6 5 number number

    // Explanation:
    // a++ converts "5" into the number 5.
    // Post-increment assigns the old numeric value (5) to b.
    // It then increments a to 6.
    // Both variables have the data type "number".
}


// 22. Predict the output.
{
    console.log(typeof (1 + "2")); // string
    console.log(typeof (1 - "2")); // number
    console.log(typeof (1 * "2")); // number
    console.log(typeof (1 / "2")); // number

    // Explanation:
    // 1 + "2" = "12" (String concatenation).
    // 1 - "2" = -1 (Numeric subtraction).
    // 1 * "2" = 2 (Numeric multiplication).
    // 1 / "2" = 0.5 (Numeric division).
}


// 23. Predict the output.
{
    let val = null;

    console.log(typeof val);  // object
    console.log(val + 1);     // 1
    console.log(val - 1);     // -1
    console.log(val * 1);     // 0
    console.log(Boolean(val)); // false

    // Explanation:
    // typeof null returns "object" due to a historical JavaScript bug.
    // During numeric operations, null converts to 0.
    //
    // null + 1 = 0 + 1 = 1
    // null - 1 = 0 - 1 = -1
    // null * 1 = 0 * 1 = 0
    //
    // null is a falsy value, so Boolean(null) returns false.
}