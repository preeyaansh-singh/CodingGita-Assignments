// JavaScript Practice – Type Conversion
// Questions 11–18


// 11. Predict the output.
{
    console.log("5" + 3 + 2); // 532
    console.log(5 + 3 + "2"); // 82
    console.log("5" - 3 + 2); // 4
    console.log(5 - "3" + "2"); // 22

    // Explanation:
    // "5" + 3 + 2 = "53" + 2 = "532"
    // 5 + 3 + "2" = 8 + "2" = "82"
    // "5" - 3 + 2 = 2 + 2 = 4
    // 5 - "3" + "2" = 2 + "2" = "22"
    // Operators with equal precedence are evaluated left to right.
}


// 12. Predict the output.
{
    console.log(true + true);    // 2
    console.log(true + false);   // 1
    console.log(true + "false"); // truefalse
    console.log(false + "true"); // falsetrue

    // Explanation:
    // true converts to 1 and false converts to 0 during numeric addition.
    // When one operand is a string, + performs string concatenation.
}


// 13. Predict the output.
{
    console.log(null + 5);        // 5
    console.log(undefined + 5);   // NaN
    console.log(null + "5");      // null5
    console.log(undefined + "5"); // undefined5

    // Explanation:
    // null converts to 0 during numeric addition.
    // undefined converts to NaN.
    // With a string operand, + performs string concatenation.
}


// 14. Predict the output.
{
    console.log([] + []); // "" (Empty String)
    console.log([] + {}); // [object Object]
    console.log({} + []); // [object Object]
    console.log({} + {}); // [object Object][object Object]

    // Explanation:
    // During addition, arrays and objects are converted to primitives.
    // [] converts to an empty string "".
    // {} converts to "[object Object]".
    //
    // "" + "" = ""
    // "" + "[object Object]" = "[object Object]"
    // "[object Object]" + "" = "[object Object]"
    // "[object Object]" + "[object Object]"
    // = "[object Object][object Object]"
    //
    // Note: These results apply to the console.log expressions shown.
    // Standalone expressions beginning with {} may be parsed differently.
}


// 15. Predict the output.
{
    let a = "10";
    let b = 5;

    let c = a + b;
    let d = a - b;
    let e = +a + b;

    console.log(c, typeof c); // 105 string
    console.log(d, typeof d); // 5 number
    console.log(e, typeof e); // 15 number

    // Explanation:
    // a + b = "10" + 5 = "105" (String concatenation).
    // a - b = 10 - 5 = 5 (Numeric subtraction).
    // +a converts "10" into the number 10.
    // Therefore, +a + b = 10 + 5 = 15.
}


// 16. Predict the output.
{
    console.log(!!"Hello");   // true
    console.log(!!"");        // false
    console.log(!!0);         // false
    console.log(!!1);         // true
    console.log(!!null);      // false
    console.log(!!undefined); // false

    // Explanation:
    // Double NOT (!!) converts a value into its boolean equivalent.
    // The first ! reverses the truthiness.
    // The second ! reverses it again.
    //
    // "Hello" and 1 are truthy.
    // "", 0, null, and undefined are falsy.
}


// 17. Predict the output.
{
    console.log(Number(""));       // 0
    console.log(Number(" "));      // 0
    console.log(Number("0"));      // 0
    console.log(Number("  25  ")); // 25
    console.log(Number("25px"));   // NaN

    // Explanation:
    // An empty string converts to 0.
    // A whitespace-only string also converts to 0.
    // "0" converts to the number 0.
    // Leading and trailing whitespace is ignored.
    // "25px" is not a valid numeric string, so it produces NaN.
}


// 18. Predict the output.
{
    let val1 = "5";
    let val2 = 2;

    console.log(val1 + val2);  // 52
    console.log(+val1 + val2); // 7
    console.log(val1 - val2);  // 3
    console.log(val1 * val2);  // 10
    console.log(val1 / val2);  // 2.5

    // Explanation:
    // "5" + 2 = "52" (String concatenation).
    // +"5" + 2 = 5 + 2 = 7 (Unary + converts string to number).
    // "5" - 2 = 3 (Numeric subtraction).
    // "5" * 2 = 10 (Numeric multiplication).
    // "5" / 2 = 2.5 (Numeric division).
}