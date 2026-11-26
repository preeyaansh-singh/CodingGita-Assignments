
// Q1. Check whether a number is even or odd

let number = 10;

if (number % 2 === 0) {
    console.log("Even Number");
} else {
    console.log("Odd Number");
}


// Q2. Check if a person is eligible to vote

let age = 20;

if (age >= 18) {
    console.log("Eligible");
} else {
    console.log("Not Eligible");
}


// Q3. Check whether a number is positive or negative

let num = -5;

if (num >= 0) {
    console.log("Positive Number");
} else {
    console.log("Negative Number");
}


// Q4. Check whether a student has passed or failed

let marks = 45;

if (marks >= 35) {
    console.log("Passed");
} else {
    console.log("Failed");
}


// Q5. Check whether a character is an uppercase letter

let character = "A";

if (character >= "A" && character <= "Z") {
    console.log("Uppercase Letter");
} else {
    console.log("Not an Uppercase Letter");
}


// Q6. Check if a number is divisible by 3

let value = 15;

if (value % 3 === 0) {
    console.log("Divisible by 3");
} else {
    console.log("Not Divisible by 3");
}


// Q7. Check password

let password = "admin123";

if (password === "admin123") {
    console.log("Login Successful");
} else {
    console.log("Incorrect Password");
}


// Q8. Check whether a year is a leap year (basic rule)

let year = 2024;

if (year % 4 === 0) {
    console.log("Leap Year");
} else {
    console.log("Not a Leap Year");
}


// Q9. Find the greater of two numbers

let firstNumber = 25;
let secondNumber = 40;

if (firstNumber > secondNumber) {
    console.log(firstNumber + " is Greater");
} else {
    console.log(secondNumber + " is Greater");
}


// Q10. Check whether a number is positive, negative, or zero

let numberToCheck = 0;

if (numberToCheck > 0) {
    console.log("Positive Number");
} else {
    if (numberToCheck < 0) {
        console.log("Negative Number");
    } else {
        console.log("Zero");
    }
}
