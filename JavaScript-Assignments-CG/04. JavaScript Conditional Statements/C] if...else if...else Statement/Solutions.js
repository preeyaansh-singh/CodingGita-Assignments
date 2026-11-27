
// Q1. Print the season based on month number

let month = 4;

if (month === 12 || month === 1 || month === 2) {
    console.log("Winter");
} else if (month >= 3 && month <= 5) {
    console.log("Summer");
} else if (month >= 6 && month <= 8) {
    console.log("Monsoon");
} else if (month >= 9 && month <= 11) {
    console.log("Autumn");
} else {
    console.log("Invalid Month");
}


// Q2. Calculate tax based on income

let income = 800000;
let tax;

if (income < 300000) {
    tax = 0;
} else if (income <= 700000) {
    tax = income * 0.05;
} else if (income <= 1000000) {
    tax = income * 0.10;
} else {
    tax = income * 0.15;
}

console.log("Tax Amount: ₹" + tax);


// Q3. Check student's score

let score = 85;

if (score >= 90) {
    console.log("Outstanding");
} else if (score >= 70) {
    console.log("Good");
} else if (score >= 40) {
    console.log("Average");
} else {
    console.log("Needs Improvement");
}


// Q4. Check vehicle speed

let speed = 65;

if (speed < 40) {
    console.log("Slow");
} else if (speed <= 80) {
    console.log("Normal");
} else {
    console.log("Fast");
}


// Q5. Check person's height

let height = 175;

if (height < 150) {
    console.log("Short");
} else if (height <= 170) {
    console.log("Average");
} else {
    console.log("Tall");
}


// Q6. Check whether a day is a Weekday or Weekend

let day = 6;

if (day >= 1 && day <= 5) {
    console.log("Weekday");
} else if (day === 6 || day === 7) {
    console.log("Weekend");
} else {
    console.log("Invalid Day");
}


// Q7. Calculate electricity bill based on units

let units = 120;
let bill;

if (units >= 0 && units <= 50) {
    bill = units * 2;
} else if (units <= 150) {
    bill = units * 4;
} else {
    bill = units * 6;
}

console.log("Electricity Bill: ₹" + bill);


// Q8. Check student's attendance percentage

let attendance = 85;

if (attendance >= 90) {
    console.log("Excellent");
} else if (attendance >= 75) {
    console.log("Good");
} else if (attendance >= 50) {
    console.log("Satisfactory");
} else {
    console.log("Poor");
}


// Q9. Find the highest mark among three subjects

let subject1 = 85;
let subject2 = 92;
let subject3 = 78;

if (subject1 >= subject2 && subject1 >= subject3) {
    console.log("Highest Mark: " + subject1);
} else if (subject2 >= subject1 && subject2 >= subject3) {
    console.log("Highest Mark: " + subject2);
} else {
    console.log("Highest Mark: " + subject3);
}


// Q10. Check whether a number is positive/negative and even/odd

let number = -7;

if (number === 0) {
    console.log("Zero");
} else if (number > 0 && number % 2 === 0) {
    console.log("Positive Even");
} else if (number > 0 && number % 2 !== 0) {
    console.log("Positive Odd");
} else if (number < 0 && number % 2 === 0) {
    console.log("Negative Even");
} else {
    console.log("Negative Odd");
}
