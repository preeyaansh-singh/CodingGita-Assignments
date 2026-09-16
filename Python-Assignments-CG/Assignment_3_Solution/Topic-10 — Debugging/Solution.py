# debugging_answers.py
# Q54 - Q59 (Debugging)

def q54_string_integer():
    print("Q54 — String and Integer Fix:")

    age = int(input("Enter age: "))
    print("Age after 5 years:", age + 5)

    print("Expected Output: depends on input (numeric addition)\n")


def q55_incorrect_quotes():
    print("Q55 — Incorrect Quotes Fix:")

    print("It's Python")

    print("Expected Output: It's Python\n")


def q56_slicing_error():
    print("Q56 — Incorrect Slicing Syntax Fix:")

    text = "Python"
    print(text[1:4])

    print("Expected Output: yth\n")


def q57_split_separator():
    print("Q57 — Incorrect split() Separator Fix:")

    a, b = input("Enter two numbers: ").split()
    print(a, b)

    print("Expected Output: depends on input (space-separated values)\n")


def q58_string_vs_numeric():
    print("Q58 — String vs Numeric Addition:")

    a, b = input("Enter two numbers: ").split()

    print("String Addition:", a + b)
    print("Numeric Addition:", int(a) + int(b))

    print("Expected Output Example:")
    print("String Addition: 1020")
    print("Numeric Addition: 30\n")


def q59_escape_sequence():
    print("Q59 — Escape Sequence Fix:")

    print("C:\\new\\test")

    print("Expected Output: C:\\new\\test\n")


# ---------------- MAIN ---------------- #

if __name__ == "__main__":
    # Uncomment input-based ones when running manually

    # q54_string_integer()
    q55_incorrect_quotes()
    q56_slicing_error()
    # q57_split_separator()
    # q58_string_vs_numeric()
    q59_escape_sequence()