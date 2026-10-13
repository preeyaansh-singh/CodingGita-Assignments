// 11. Predict the output.
{
    let x = 10;
    let y = x++;
    let z = ++x;

    console.log(x, y, z); // 12 10 12

    // Explanation:
    // Initially, x = 10.
    // y = x++ assigns 10 to y, then x becomes 11.
    // z = ++x increments x to 12, then assigns 12 to z.
    // Final values: x = 12, y = 10, z = 12.
}


// 12. Predict the output.
{
    let a = 5;
    let b = a-- + ++a;

    console.log(a, b); // 5 10

    // Explanation:
    // Initially, a = 5.
    // a-- returns 5, then a becomes 4.
    // ++a increments a to 5, then returns 5.
    // b = 5 + 5 = 10.
    // Final values: a = 5, b = 10.
}


// 13. Predict the output.
{
    let m = 7;
    let n = --m + m++;

    console.log(m, n); // 7 12

    // Explanation:
    // Initially, m = 7.
    // --m decreases m to 6, then returns 6.
    // m++ returns 6, then increases m to 7.
    // n = 6 + 6 = 12.
    // Final values: m = 7, n = 12.
}


// 14. Predict the output.
{
    let p = 3;
    let q = p++ + ++p + p;

    console.log(p, q); // 5 13

    // Explanation:
    // Initially, p = 3.
    // p++ returns 3, then p becomes 4.
    // ++p increments p to 5, then returns 5.
    // The last p evaluates to 5.
    // q = 3 + 5 + 5 = 13.
    // Final values: p = 5, q = 13.
}


// 15. Predict the output.
{
    let val = 0;
    val = val++ + ++val;

    console.log(val); // 2

    // Explanation:
    // Initially, val = 0.
    // val++ returns 0, then val becomes 1.
    // ++val increments val to 2, then returns 2.
    // The expression becomes 0 + 2 = 2.
    // Finally, 2 is assigned back to val.
    // Final value: val = 2.
}
