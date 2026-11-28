
// Q1. Find the number of days in a month

let month = 2;

switch (month) {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
        console.log("31 Days");
        break;

    case 4:
    case 6:
    case 9:
    case 11:
        console.log("30 Days");
        break;

    case 2:
        console.log("28 Days");
        break;

    default:
        console.log("Invalid Month");
}


// Q2. Check whether a character is a vowel or consonant

let character = "A";
character = character.toLowerCase();

switch (character) {
    case "a":
    case "e":
    case "i":
    case "o":
    case "u":
        console.log("Vowel");
        break;

    default:
        if (character.length === 1 && character >= "a" && character <= "z") {
            console.log("Consonant");
        } else {
            console.log("Invalid Character");
        }
}


// Q3. Print season using multiple cases

let season = 3;

switch (season) {
    case 1:
    case 2:
        console.log("Winter");
        break;

    case 3:
    case 4:
        console.log("Summer");
        break;

    default:
        console.log("Invalid Number");
}


// Q4. Assign class based on marks

let marks = 82;

switch (true) {
    case marks >= 75:
        console.log("Distinction");
        break;

    case marks >= 60:
        console.log("1st Class");
        break;

    case marks >= 50:
        console.log("2nd Class");
        break;

    case marks >= 35:
        console.log("3rd Class");
        break;

    default:
        console.log("Failed");
}


// Q5. Nested switch for user roles

let role = "admin";
let action = "edit";

switch (role) {
    case "admin":
        switch (action) {
            case "create":
                console.log("Content Created");
                break;

            case "edit":
                console.log("Content Edited");
                break;

            case "delete":
                console.log("Content Deleted");
                break;

            default:
                console.log("Invalid Action");
        }
        break;

    case "user":
        console.log("Limited Access");
        break;

    default:
        console.log("Invalid Role");
}


// Q6. Correct the fruit program

// Original Output:
// Mango is yellow
// Banana is yellow
// Unknown fruit

// This happens because there are no break statements.
// This behaviour is called fall-through.

// Corrected Code:

let fruit = "mango";

switch (fruit) {
    case "apple":
        console.log("Apple is red");
        break;

    case "mango":
        console.log("Mango is yellow");
        break;

    case "banana":
        console.log("Banana is yellow");
        break;

    default:
        console.log("Unknown fruit");
}


// Q7. Identify different values using switch

let value = "0";

switch (value) {
    case 0:
        console.log("Number Zero");
        break;

    case "0":
        console.log("String Zero");
        break;

    case false:
        console.log("Boolean False");
        break;

    case null:
        console.log("Null Value");
        break;

    case undefined:
        console.log("Undefined Value");
        break;

    default:
        console.log("Unknown Value");
}

// Switch uses strict equality (===).
// It compares both value and data type.
// Therefore, 0 and "0" are different values.


// Q8. Calculator using switch

let num1 = 20;
let num2 = 5;
let operator = "/";

switch (operator) {
    case "+":
        console.log(num1 + num2);
        break;

    case "-":
        console.log(num1 - num2);
        break;

    case "*":
        console.log(num1 * num2);
        break;

    case "/":
        if (num2 === 0) {
            console.log("Cannot Divide by Zero");
        } else {
            console.log(num1 / num2);
        }
        break;

    case "%":
        if (num2 === 0) {
            console.log("Cannot Find Remainder with Zero");
        } else {
            console.log(num1 % num2);
        }
        break;

    case "**":
        console.log(num1 ** num2);
        break;

    default:
        console.log("Invalid Operator");
}


// Q9. Check the position of a day in a month

let date = 15;

switch (true) {
    case date >= 1 && date <= 10:
        console.log("Beginning of the month");
        break;

    case date >= 11 && date <= 20:
        console.log("Middle of the month");
        break;

    case date >= 21 && date <= 31:
        console.log("End of the month");
        break;

    default:
        console.log("Invalid Date");
}


// Q10. Online food ordering system

let category = "veg";
let item = "paneer";
let size = "full";
let price = 0;

switch (category) {
    case "veg":
        switch (item) {
            case "paneer":
                switch (size) {
                    case "half":
                        price = 120;
                        break;

                    case "full":
                        price = 220;
                        break;

                    default:
                        console.log("Invalid Size");
                }
                break;

            case "biryani":
                switch (size) {
                    case "half":
                        price = 100;
                        break;

                    case "full":
                        price = 180;
                        break;

                    default:
                        console.log("Invalid Size");
                }
                break;

            default:
                console.log("Invalid Veg Item");
        }
        break;

    case "nonveg":
        switch (item) {
            case "chicken":
                switch (size) {
                    case "half":
                        price = 180;
                        break;

                    case "full":
                        price = 320;
                        break;

                    default:
                        console.log("Invalid Size");
                }
                break;

            case "fish":
                switch (size) {
                    case "half":
                        price = 200;
                        break;

                    case "full":
                        price = 350;
                        break;

                    default:
                        console.log("Invalid Size");
                }
                break;

            default:
                console.log("Invalid Nonveg Item");
        }
        break;

    default:
        console.log("Invalid Category");
}

if (price > 0) {
    console.log("Order Summary");
    console.log("Category: " + category);
    console.log("Item: " + item);
    console.log("Size: " + size);
    console.log("Total Price: ₹" + price);
}
