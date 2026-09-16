# integrated_problems_answers.py
# Q60 - Q70 (Integrated Problems)

def q60_student_result():
    print("Q60 — Student Result Information:")

    name = input("Enter name: ")
    m1, m2, m3 = map(int, input("Enter 3 marks: ").split())

    total = m1 + m2 + m3
    avg = total / 3

    print(f"Name: {name}")
    print(f"Total: {total}")
    print(f"Average: {avg:.2f}")

    print("\nExpected Output Example:")
    print("Name: Rahul")
    print("Total: 240")
    print("Average: 80.00\n")


def q61_student_id():
    print("Q61 — Student ID Analyzer:")

    sid = input("Enter ID: ")
    degree, batch, branch, roll = sid.split("-")

    print(f"Degree: {degree}")
    print(f"Batch: {batch}")
    print(f"Branch: {branch}")
    print(f"Roll Number: {int(roll)}")

    print("Last 3 characters:", sid[-3:])

    print("\nExpected Output Example:")
    print("Degree: BTECH")
    print("Batch: 24")
    print("Branch: CSE")
    print("Roll Number: 105\n")


def q62_username():
    print("Q62 — Username Generator:")

    name = input("Enter full name: ").split()
    username = name[0].lower() + "." + name[2].lower()

    print("Username:", username)

    print("\nExpected Output: rahul.sharma\n")


def q63_sentence_info():
    print("Q63 — Sentence Information:")

    words = input("Enter sentence: ").split()

    print("First word:", words[0])
    print("Last word:", words[-1])
    print("Total words:", len(words))

    print("\nExpected Output Example:")
    print("First word: Python")
    print("Last word: powerful")
    print("Total words: 4\n")


def q64_email_analyzer():
    print("Q64 — Email Analyzer:")

    email = input("Enter email: ")

    print("@ Present:", "@" in email)

    username, domain = email.split("@")
    print("Username:", username)
    print("Domain:", domain)

    print("\nExpected Output Example:")
    print("@ Present: True")
    print("Username: rahul")
    print("Domain: gmail.com\n")


def q65_character_analyzer():
    print("Q65 — Character Analyzer:")

    ch = input("Enter character: ")

    print("Character:", ch)
    print("Code:", ord(ch))
    print("Previous:", chr(ord(ch) - 1))
    print("Next:", chr(ord(ch) + 1))

    print("\nExpected Output Example:")
    print("Character: B")
    print("Code: 66")
    print("Previous: A")
    print("Next: C\n")


def q66_product_bill():
    print("Q66 — Product Bill:")

    product = input("Product: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    discount = float(input("Discount %: "))

    subtotal = price * quantity
    discount_amt = subtotal * discount / 100
    final = subtotal - discount_amt

    print(f"Product: {product}")
    print(f"Price: {price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Discount: {discount_amt:.2f}")
    print(f"Final Total: {final:.2f}")

    print("\nExpected Output Example:")
    print("Product: Pen")
    print("Price: 20.00")
    print("Quantity: 5")
    print("Subtotal: 100.00")
    print("Discount: 10.00")
    print("Final Total: 90.00\n")


def q67_date_analyzer():
    print("Q67 — Date Analyzer:")

    date = input("Enter date (DD-MM-YYYY): ")
    day, month, year = date.split("-")

    print("Day:", day)
    print("Month:", month)
    print("Year:", year)

    print("Year (slicing):", date[-4:])

    print("\nExpected Output:")
    print("Day: 09")
    print("Month: 09")
    print("Year: 2026\n")


def q68_string_transform():
    print("Q68 — String Transformation:")

    text = input("Enter text: ").split()

    first = text[0]
    second = text[1]

    print("First Word:", first)
    print("Second Word:", second)
    print("First Word Reversed:", first[::-1])
    print("Second Word Reversed:", second[::-1])

    print("\nExpected Output Example:")
    print("First Word: Python")
    print("Second Word: Programming")
    print("First Word Reversed: nohtyP")
    print("Second Word Reversed: gnimmargorP\n")


def q69_code_formatter():
    print("Q69 — Student Code Formatter:")

    data = input("Enter code: ").split("-")

    degree = data[0]
    batch = data[1]
    branch = data[2]
    roll = data[3]

    print(f"Degree: {degree}")
    print(f"Batch: {batch}")
    print(f"Branch: {branch}")
    print(f"Roll: {roll}")
    print(f"Code: {degree}/{branch}/{roll}")

    print("\nExpected Output Example:")
    print("Degree: BTECH")
    print("Batch: 2026")
    print("Branch: CSE")
    print("Roll: 105")
    print("Code: BTECH/CSE/105\n")


def q70_final_challenge():
    print("Q70 — Final Challenge:")

    full = input("Enter full name: ")
    parts = full.split()

    first = parts[0]
    last = parts[-1]

    print(f"Original: {full}")
    print(f"First Name: {first}")
    print(f"Last Name: {last}")
    print(f"First Name (Upper Part): {first[:3].upper()}")
    print(f"Last Name (Lower Part): {last[1:4].lower()}")
    print(f"Full Name Reversed: {full[::-1]}")

    print("\nExpected Output Example:")
    print("Original: Rahul Kumar Sharma")
    print("First Name: Rahul")
    print("Last Name: Sharma")
    print("First Name (Upper Part): RAH")
    print("Last Name (Lower Part): har")
    print("Full Name Reversed: amrahS ramuK luhaR\n")


# ---------------- MAIN ---------------- #

if __name__ == "__main__":
    # Uncomment as needed

    # q60_student_result()
    # q61_student_id()
    # q62_username()
    # q63_sentence_info()
    # q64_email_analyzer()
    # q65_character_analyzer()
    # q66_product_bill()
    # q67_date_analyzer()
    # q68_string_transform()
    # q69_code_formatter()
    # q70_final_challenge()

    print("Run individual functions by uncommenting them.")