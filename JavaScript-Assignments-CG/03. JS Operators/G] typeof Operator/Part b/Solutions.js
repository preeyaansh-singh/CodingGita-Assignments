// 6. Predict the output.
{
    console.log(typeof 42);        // number
    console.log(typeof "Hello");   // string
    console.log(typeof true);      // boolean
    console.log(typeof undefined); // undefined

    // Explanation:
    // 42 is a number.
    // "Hello" is a string.
    // true is a boolean.
    // undefined represents an undefined value.
}


// 7. Predict the output.
{
    console.log(typeof null); // object
    console.log(typeof {});   // object
    console.log(typeof []);   // object

    // Explanation:
    // typeof null returns "object" due to a historical JavaScript bug.
    // {} is an object.
    // Arrays are also classified as objects in JavaScript.
}


// 8. Predict the output.
{
    console.log(typeof NaN);          // number
    console.log(typeof Infinity);     // number
    console.log(typeof function(){}); // function

    // Explanation:
    // NaN (Not-a-Number) has the type "number".
    // Infinity is also a numeric value.
    // typeof returns "function" for functions.
}


// 9. Create three variables and print their types
// with a clear message.
{
    let price = 99.99;
    let message = "Welcome";
    let isActive = false;

    console.log("Type of price:", typeof price);
    // Output: Type of price: number

    console.log("Type of message:", typeof message);
    // Output: Type of message: string

    console.log("Type of isActive:", typeof isActive);
    // Output: Type of isActive: boolean
}


// 10. Predict the output.
{
    let value = null;

    console.log(typeof value);              // object
    console.log(typeof value === "object"); // false

    // Explanation:
    // typeof null returns the string "object".
    // Therefore, typeof value === "object" evaluates to true.
    // However, null is a primitive value, not an actual object.
}