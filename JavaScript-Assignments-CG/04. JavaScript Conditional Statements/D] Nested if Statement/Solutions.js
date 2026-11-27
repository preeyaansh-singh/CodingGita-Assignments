
// Q1. Check if a number is greater than 10 and divisible by 3

let number = 15;

if (number > 10) {
    if (number % 3 === 0) {
        console.log("Greater than 10 and Divisible by 3");
    } else {
        console.log("Greater than 10 but Not Divisible by 3");
    }
} else {
    console.log("Number is not greater than 10");
}


// Q2. Check voting eligibility using age and voter ID

let age = 20;
let hasVoterID = true;

if (age >= 18) {
    if (hasVoterID === true) {
        console.log("Can Vote");
    } else {
        console.log("Voter ID Required");
    }
} else {
    console.log("Not Eligible");
}


// Q3. Check student marks and distinction

let marks = 85;

if (marks >= 40) {
    if (marks >= 80) {
        console.log("Passed with Distinction");
    } else {
        console.log("Passed");
    }
} else {
    console.log("Failed");
}


// Q4. Simple ATM system

let correctPIN = 1234;
let enteredPIN = 1234;
let balance = 5000;
let withdrawalAmount = 2000;

if (enteredPIN === correctPIN) {
    if (balance >= withdrawalAmount) {
        balance = balance - withdrawalAmount;
        console.log("Withdrawal Successful");
        console.log("Remaining Balance: ₹" + balance);
    } else {
        console.log("Insufficient Balance");
    }
} else {
    console.log("Incorrect PIN");
}


// Q5. Check whether a year is a leap year

let year = 2000;

if (year % 4 === 0) {
    if (year % 100 === 0) {
        if (year % 400 === 0) {
            console.log("Leap Year");
        } else {
            console.log("Not a Leap Year");
        }
    } else {
        console.log("Leap Year");
    }
} else {
    console.log("Not a Leap Year");
}


// Q6. Check whether an email is valid

let email = "student@gmail.com";

if (email.includes("@")) {
    if (email.endsWith(".com")) {
        if (email.length > 10) {
            console.log("Valid Email");
        } else {
            console.log("Email is too short");
        }
    } else {
        console.log("Email must end with .com");
    }
} else {
    console.log("Invalid Email");
}


// Q7. Online shopping discount system

let cartTotal = 2000;
let isPremiumMember = true;
let discount;
let finalAmount;

if (cartTotal >= 1000) {
    if (isPremiumMember === true) {
        discount = cartTotal * 0.20;
    } else {
        discount = cartTotal * 0.10;
    }

    finalAmount = cartTotal - discount;

    console.log("Discount: ₹" + discount);
    console.log("Final Amount: ₹" + finalAmount);
} else {
    console.log("No Discount Available");
    console.log("Final Amount: ₹" + cartTotal);
}


// Q8. Check positive, even and divisible by 4

let num = 16;

if (num > 0) {
    if (num % 2 === 0) {
        if (num % 4 === 0) {
            console.log("Positive Even and Divisible by 4");
        } else {
            console.log("Positive Even but Not Divisible by 4");
        }
    } else {
        console.log("Positive Odd Number");
    }
} else {
    console.log("Number is not Positive");
}


// Q9. Job eligibility checker

let candidateAge = 25;
let hasDegree = true;
let experience = 3;

if (candidateAge >= 21 && candidateAge <= 30) {
    if (hasDegree === true) {
        if (experience >= 2) {
            console.log("Eligible for Interview");
        } else {
            console.log("Not Enough Experience");
        }
    } else {
        console.log("Graduation Degree Required");
    }
} else {
    console.log("Age Criteria Not Satisfied");
}


// Q10. Check eligibility for final exam

let isPresent = true;
let internalMarks = 35;
let externalMarks = 40;

if (isPresent === true) {
    if (internalMarks >= 30) {
        if (externalMarks >= 35) {
            console.log("Eligible for Final Exam");
        } else {
            console.log("External Marks Not Sufficient");
        }
    } else {
        console.log("Internal Marks Not Sufficient");
    }
} else {
    console.log("Student is Absent");
}
