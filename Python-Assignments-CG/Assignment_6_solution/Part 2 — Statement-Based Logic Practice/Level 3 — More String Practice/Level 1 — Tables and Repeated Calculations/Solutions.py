# Q86. Count Words
s=input()
print(len(s.split()))

# Q87. Replace All 'a' with 'e'
s=input()
print(s.replace("a","e"))

# Q88. Check for a Character
s=input()
ch=input()
print(ch in s)

# Q89. Compare Two Strings
s1=input()
s2=input()
print(s1==s2)

# Q90. Count Digits in a String
s=input()
count=0
for ch in s:
    if "0"<=ch<="9":
        count+=1
print(count)

# Q91. Count Uppercase Letters
s=input()
count=0
for ch in s:
    if "A"<=ch<="Z":
        count+=1
print(count)

# Q92. Count Lowercase Letters
s=input()
count=0
for ch in s:
    if "a"<=ch<="z":
        count+=1
print(count)

# Q93. Remove All Vowels
s=input()
result=""
for ch in s:
    if ch.lower() not in "aeiou":
        result+=ch
print(result)

# Q94. Remove All Digits
s=input()
result=""
for ch in s:
    if not ("0"<=ch<="9"):
        result+=ch
print(result)

# Q95. Toggle Character Case
s=input()
result=""
for ch in s:
    if "a"<=ch<="z":
        result+=ch.upper()
    elif "A"<=ch<="Z":
        result+=ch.lower()
    else:
        result+=ch
print(result)