# Q45. Find the Middle Character
s=input()
middle=len(s)//2
print(s[middle])

# Q46. First Half and Second Half
s=input()
middle=len(s)//2
print("First Half:",s[:middle])
print("Second Half:",s[middle:])

# Q47. Split a String by Length — Odd vs Even
s=input()
n=len(s)
middle=n//2
first=""
second=""
for i in range(n):
    if i<middle:
        first+=s[i]
    elif i==middle and n%2!=0:
        mid=s[i]
    else:
        second+=s[i]
print("First Half:",first)
if n%2!=0:
    print("Middle:",mid)
print("Second Half:",second)

# Q48. Compare Two Halves
s=input()
middle=len(s)//2
equal=True
for i in range(middle):
    if s[i]!=s[i+middle]:
        equal=False
        break
if equal:
    print("Equal Halves")
else:
    print("Different Halves")

# Q49. Mirror the String
s=input()
symmetric=True
for i in range(len(s)//2):
    if s[i]!=s[-(i+1)]:
        symmetric=False
        break
if symmetric:
    print("Symmetric")
else:
    print("Not Symmetric")

# Q50. Alternate Character Extraction
s=input()
result=""
for i in range(0,len(s),2):
    result+=s[i]
print(result)

# Q51. Count Characters at Even and Odd Indexes
s=input()
even=0
odd=0
for i in range(len(s)):
    if i%2==0:
        even+=1
    else:
        odd+=1
print(f"Even Index = {even}, Odd Index = {odd}")

# Q52. Swap Adjacent Characters
s=input()
result=""
for i in range(0,len(s),2):
    result+=s[i+1]+s[i]
print(result)