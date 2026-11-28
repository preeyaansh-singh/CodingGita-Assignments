
// Q1. Check if a number is divisible by 7

let number = 21;

let result1 = number % 7 === 0
    ? "Divisible by 7"
    : "Not Divisible by 7";

console.log(result1);


// Q2. Check the temperature

let temperature = 32;

let result2 = temperature >= 30
    ? "Hot Day"
    : "Pleasant Day";

console.log(result2);


// Q3. Check whether a string is empty

let str = "";

let result3 = str === ""
    ? "Empty String"
    : "String has content";

console.log(result3);


// Q4. Classify a person based on age

let age = 18;

let result4 = age < 13 ? "Child"
    : age < 20 ? "Teenager"
    : "Adult";

console.log(result4);


// Q5. Find the greatest of three numbers

let a = 25;
let b = 40;
let c = 30;

let greatest = a >= b
    ? (a >= c ? a : c)
    : (b >= c ? b : c);

console.log("Greatest Number: " + greatest);


// Q6. Classify student's marks

let marks = 72;

let result6 = marks >= 75 ? "Distinction"
    : marks >= 60 ? "First Class"
    : marks >= 50 ? "Second Class"
    : marks >= 35 ? "Pass"
    : "Fail";

console.log(result6);


// Q7. Check positive, negative, even, odd or zero

let num = -8;

let result7 = num === 0 ? "Zero"
    : num > 0
        ? (num % 2 === 0 ? "Positive Even" : "Positive Odd")
        : (num % 2 === 0 ? "Negative Even" : "Negative Odd");

console.log(result7);


// Q8. Check whether a year is a leap year

let year = 2000;

let result8 = year % 4 === 0
    ? (year % 100 === 0
        ? (year % 400 === 0 ? "Leap Year" : "Not a Leap Year")
        : "Leap Year")
    : "Not a Leap Year";

console.log(result8);


// Q9. Check user role and action

let role = "admin";
let action = "delete";

let result9 = role === "admin"
    ? (action === "delete" ? "Admin Delete"
        : action === "edit" ? "Admin Edit"
        : "Admin Other")
    : role === "user"
        ? (action === "view" ? "User View" : "User Restricted")
        : "Invalid Role";

console.log(result9);


// Q10. Calculate discount and final payable amount

let cartTotal = 6000;

let result10 = cartTotal >= 5000
    ? { discount: "20%", finalAmount: cartTotal * 0.80 }
    : cartTotal >= 2000
        ? { discount: "10%", finalAmount: cartTotal * 0.90 }
        : cartTotal >= 1000
            ? { discount: "5%", finalAmount: cartTotal * 0.95 }
            : { discount: "0%", finalAmount: cartTotal };

console.log("Discount: " + result10.discount);
console.log("Final Amount: ₹" + result10.finalAmount);
