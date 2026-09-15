# unicode_and_chars_answers.py
# Answers for Q12 - Q18 (character codes, chr/ord, comparisons, unicode challenge)

def q12_find_character_codes():
    print("Q12 — Find Character Codes using ord():")
    items = ['A', 'a', 'Z', 'z', '0', '9', '@']
    for ch in items:
        print(f"ord('{ch}') ->", ord(ch))
    print()

def q13_convert_codes_to_characters():
    print("Q13 — Convert Codes to Characters using chr():")
    codes = [65, 66, 97, 98, 48, 57, 64]
    for c in codes:
        print(f"chr({c}) ->", chr(c))
    print()

def q14_upper_lowercase_analysis():
    print("Q14 — Uppercase and Lowercase (ord values):")
    pairs = [('A','a'), ('B','b')]
    for upper, lower in pairs:
        ou = ord(upper); ol = ord(lower)
        diff = ol - ou
        print(f"ord('{upper}') = {ou}, ord('{lower}') = {ol}, difference (lower-upper) = {diff}")
    print("Answers:")
    print("1) ord('a') is larger than ord('A').")
    print("2) The difference is", ord('a') - ord('A'))
    print("3) Yes — difference is the same for 'B' and 'b' (also 32).")
    print()

def q15_character_code_program_demo():
    print("Q15 — Character Code Program (demo test-cases):")
    test_inputs = ['A', 'a', '0']
    for ch in test_inputs:
        print(f"Input: '{ch}' -> ord ->", ord(ch))
    print("Interactive version (uncomment input() lines in the script to accept input).")
    print()

def q16_next_character_demo():
    print("Q16 — Next Character (uppercase letter -> next uppercase):")
    test_inputs = ['A', 'C', 'Y']
    for ch in test_inputs:
        code = ord(ch)
        # If already 'Z' (90), keep as 'Z' to avoid going outside uppercase letters.
        next_code = code + 1 if code < ord('Z') else ord('Z')
        next_ch = chr(next_code)
        print(f"Input: {ch} -> Next: {next_ch}")
    print()

def q17_character_comparison_and_unicode():
    print("Q17 — Character Comparison and Unicode (predictions + ord() to explain):")
    exprs = [
        ('A' < 'B'),
        ('a' < 'b'),
        ('A' < 'a'),
        ('0' < '9'),
    ]
    # print predicted results (actual Python evaluation)
    print("Evaluations:")
    print("'A' < 'B' ->", exprs[0])
    print("'a' < 'b' ->", exprs[1])
    print("'A' < 'a' ->", exprs[2])
    print("'0' < '9' ->", exprs[3])
    print()
    print("Explain with ord():")
    checks = ["A","B","a","b","0","9"]
    for ch in checks:
        print(f"ord('{ch}') = {ord(ch)}")
    print("Because ord('A') < ord('a'), 'A' compares as smaller than 'a'.")
    print()

def q18_unicode_character_challenge():
    print("Q18 — Unicode Character Challenge using chr() then ord() to verify:")
    codes = [9731, 9829, 8377]
    for c in codes:
        ch = chr(c)
        print(f"chr({c}) -> {ch}   verified ord ->", ord(ch))
    print()

if __name__ == "__main__":
    q12_find_character_codes()
    q13_convert_codes_to_characters()
    q14_upper_lowercase_analysis()
    q15_character_code_program_demo()
    q16_next_character_demo()
    q17_character_comparison_and_unicode()
    q18_unicode_character_challenge()


'''Q12 — Find Character Codes using ord():
ord('A') -> 65
ord('a') -> 97
ord('Z') -> 90
ord('z') -> 122
ord('0') -> 48
ord('9') -> 57
ord('@') -> 64

Q13 — Convert Codes to Characters using chr():
chr(65) -> A
chr(66) -> B
chr(97) -> a
chr(98) -> b
chr(48) -> 0
chr(57) -> 9
chr(64) -> @

Q14 — Uppercase and Lowercase (ord values):
ord('A') = 65, ord('a') = 97, difference (lower-upper) = 32
ord('B') = 66, ord('b') = 98, difference (lower-upper) = 32
Answers:
1) ord('a') is larger than ord('A').
2) The difference is 32
3) Yes — difference is the same for 'B' and 'b' (also 32).

Q15 — Character Code Program (demo test-cases):
Input: 'A' -> ord -> 65
Input: 'a' -> ord -> 97
Input: '0' -> ord -> 48
Interactive version (uncomment input() lines in the script to accept input).

Q16 — Next Character (uppercase letter -> next uppercase):
Input: A -> Next: B
Input: C -> Next: D
Input: Y -> Next: Z

Q17 — Character Comparison and Unicode (predictions + ord() to explain):
Evaluations:
'A' < 'B' -> True
'a' < 'b' -> True
'A' < 'a' -> True
'0' < '9' -> True

Explain with ord():
ord('A') = 65
ord('B') = 66
ord('a') = 97
ord('b') = 98
ord('0') = 48
ord('9') = 57
Because ord('A') < ord('a'), 'A' compares as smaller than 'a'.

Q18 — Unicode Character Challenge using chr() then ord() to verify:
chr(9731) -> ☃   verified ord -> 9731
chr(9829) -> ♥   verified ord -> 9829
chr(8377) -> ₹   verified ord -> 8377'''