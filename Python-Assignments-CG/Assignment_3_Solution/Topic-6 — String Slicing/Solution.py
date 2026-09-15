# string_slicing_answers.py
# Q24 - Q31 (String Slicing)

def q24_basic_slicing():
    text = "PYTHON"
    print("Q24 — Basic Slicing:")
    print(text[0:3])  # PYT
    print(text[2:5])  # THO
    print(text[1:6])  # YTHON
    print()


def q25_start_stop():
    text = "PROGRAMMING"
    print("Q25 — Start and Stop:")
    print(text[:4])   # PROG
    print(text[4:])   # RAMMING
    print(text[:])    # PROGRAMMING
    print()


def q26_negative_slicing():
    text = "COMPUTER"
    print("Q26 — Negative Slicing:")
    print(text[-5:])   # PUTER
    print(text[:-3])   # COMPU
    print(text[-6:-2]) # MPUT
    print()


def q27_step_slicing():
    text = "PYTHON"
    print("Q27 — Step in Slicing:")
    print(text[::2])   # PTO
    print(text[1::2])  # YHN
    print(text[::-1])  # NOHTYP
    print()


def q28_reverse_string():
    print("Q28 — Reverse String (demo):")
    test_cases = ["Python", "Hello", "12345"]
    
    for s in test_cases:
        print(f"{s} -> {s[::-1]}")
    print()


def q29_alternate_characters():
    print("Q29 — Alternate Characters (step = 2):")
    test_cases = ["ABCDEFGH", "Python", "12345678"]
    
    for s in test_cases:
        print(f"{s} -> {s[::2]}")
    print()


def q30_first_last_three():
    print("Q30 — First and Last Three Characters:")
    test_cases = ["Programming", "Computer", "Python"]
    
    for s in test_cases:
        print(f"{s} -> First: {s[:3]}, Last: {s[-3:]}")
    print()


def q31_slicing_challenge():
    text = "ABCDEFGHIJ"
    print("Q31 — Slicing Challenge:")
    
    print("text[2:8:2]  ->", text[2:8:2])   # CEG
    print("text[8:2:-2] ->", text[8:2:-2])  # IGE
    print("text[::-2]   ->", text[::-2])    # JHFDB
    print()
    
    print("Breakdown:")
    print("1) text[2:8:2]  -> start=2, stop=8, step=2")
    print("2) text[8:2:-2] -> start=8, stop=2, step=-2")
    print("3) text[::-2]   -> start=end, stop=start, step=-2")
    print()


if __name__ == "__main__":
    q24_basic_slicing()
    q25_start_stop()
    q26_negative_slicing()
    q27_step_slicing()
    q28_reverse_string()
    q29_alternate_characters()
    q30_first_last_three()
    q31_slicing_challenge()

# Q32 — Slice Without Counting from the Beginning

text = "BTECH-CSE-2026"

print(text[:5])     # BTECH
print(text[6:9])    # CSE
print(text[-4:])    # 2026

'''Q24:
PYT
THO
YTHON

Q25:
PROG
RAMMING
PROGRAMMING

Q26:
UTER
COMPU
MPUT

Q27:
PTO
YHN
NOHTYP

Q28:
Python -> nohtyP
Hello -> olleH
12345 -> 54321

Q29:
ABCDEFGH -> ACEG
Python -> Pto
12345678 -> 1357

Q30:
Programming -> Pro ing
Computer -> Com ter
Python -> Pyt hon

Q31:
CEG
IGE
JHFDB

Q32
BTECH
CSE
2026'''