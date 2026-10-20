# Q76. Length of a String
s=input()
print(len(s))

# Q77. Print Each Character
s=input()
for ch in s:
    print(ch)

# Q78. Count Vowels
s=input()
count=0
for ch in s:
    if ch.lower() in "aeiou":
        count+=1
print(count)

# Q79. Count Consonants
s=input()
count=0
for ch in s:
    if ch.lower() in "abcdefghijklmnopqrstuvwxyz" and ch.lower() not in "aeiou":
        count+=1
print(count)

# Q80. Convert to Uppercase
s=input()
print(s.upper())

# Q81. Convert to Lowercase
s=input()
print(s.lower())

# Q82. Reverse a String
s=input()
reverse=""
for ch in s:
    reverse=ch+reverse
print(reverse)

# Q83. Palindrome String
s=input()
reverse=""
for ch in s:
    reverse=ch+reverse
print(s==reverse)

# Q84. Count a Specific Character
s=input()
count=0
for ch in s:
    if ch=="a" or ch=="A":
        count+=1
print(count)

# Q85. Remove All Spaces
s=input()
result=""
for ch in s:
    if ch!=" ":
        result+=ch
print(result)