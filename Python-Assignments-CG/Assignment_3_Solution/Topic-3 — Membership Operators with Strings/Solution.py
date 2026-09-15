# membership_answers.py
# Q7 - Q11: Membership operators with strings (examples + test cases)

def q7_basic_membership():
    text = "Python Programming"
    print("Q7 — Basic Membership (text = 'Python Programming'):")
    print("Python in text ->", "Python" in text)
    print("Java in text   ->", "Java" in text)
    print("Python not in text ->", "Python" not in text)
    print()

def q8_character_membership():
    word = "computer"
    print("Q8 — Character Membership (word = 'computer'):")
    print("'p' in word ->", "p" in word)        # True
    print("'x' in word ->", "x" in word)        # False
    print("'c' not in word ->", "c" not in word) # False because 'c' is present
    print()

def q9_case_sensitivity_in_membership():
    text = "Python"
    print("Q9 — Case Sensitivity in Membership (text = 'Python'):")
    print("'P' in text ->", "P" in text)
    print("'p' in text ->", "p" in text)
    print("'Python' in text ->", "Python" in text)
    print("'python' in text ->", "python" in text)
    print("Note: membership is case-sensitive, so 'P' != 'p' and 'Python' != 'python'.")
    print()

def q10_membership_with_user_input_tests():
    # Provided test cases (non-interactive demonstration)
    test_inputs = ["apple", "Python", "banana"]
    print("Q10 — Membership with User Input (check if 'a' occurs):")
    for s in test_inputs:
        print(f"Input: {s:7} -> 'a' in input? ->", ("a" in s))
    print()
    # If you'd like to test interactively, uncomment and run this:
    # user_text = input("Enter a word or sentence: ")
    # print("'a' in your input ->", "a" in user_text)

def q11_email_symbol_check_tests():
    # Provided test cases (non-interactive demonstration)
    test_emails = ["rahul@gmail.com", "student@yahoo.com", "rahulgmail.com"]
    print("Q11 — Email Symbol Check (check for '@'):")
    for e in test_emails:
        print(f"Input: {e:20} -> '@' present? ->", ("@" in e))
    print()
    # Interactive version (not auto-run):
    # email = input("Enter an email address: ")
    # print("Contains '@' ->", "@" in email)

if __name__ == "__main__":
    q7_basic_membership()
    q8_character_membership()
    q9_case_sensitivity_in_membership()
    q10_membership_with_user_input_tests()
    q11_email_symbol_check_tests()


'''Q7 — Basic Membership (text = 'Python Programming'):
Python in text -> True
Java in text   -> False
Python not in text -> False

Q8 — Character Membership (word = 'computer'):
'p' in word -> True
'x' in word -> False
'c' not in word -> False

Q9 — Case Sensitivity in Membership (text = 'Python'):
'P' in text -> True
'p' in text -> False
'Python' in text -> True
'python' in text -> False
Note: membership is case-sensitive, so 'P' != 'p' and 'Python' != 'python'.

Q10 — Membership with User Input (check if 'a' occurs):
Input: apple   -> 'a' in input? -> True
Input: Python  -> 'a' in input? -> False
Input: banana  -> 'a' in input? -> True

Q11 — Email Symbol Check (check for '@'):
Input: rahul@gmail.com    -> '@' present? -> True
Input: student@yahoo.com  -> '@' present? -> True
Input: rahulgmail.com     -> '@' present? -> False'''