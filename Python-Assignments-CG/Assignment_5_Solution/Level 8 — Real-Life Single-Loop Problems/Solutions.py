# Q62. Daily Expense Analyzer
n=int(input())
total=0
highest=0
lowest=float("inf")
for i in range(n):
    expense=int(input())
    total+=expense
    if expense>highest:
        highest=expense
    if expense<lowest:
        lowest=expense
print("Total:",total)
print("Highest:",highest)
print("Lowest:",lowest)

# Q63. Student Marks Analyzer
n=int(input())
total=0
highest=0
lowest=float("inf")
for i in range(n):
    marks=int(input())
    total+=marks
    if marks>highest:
        highest=marks
    if marks<lowest:
        lowest=marks
print("Total:",total)
print("Average:",total/n)
print("Highest:",highest)
print("Lowest:",lowest)

# Q64. Attendance Analyzer
n=int(input())
present=0
absent=0
for i in range(n):
    status=input()
    if status=="P":
        present+=1
    elif status=="A":
        absent+=1
print("Present:",present)
print("Absent:",absent)
print(f"Attendance: {present/n*100:.2f}%")

# Q65. Electricity Usage Analyzer
n=int(input())
total=0
count=0
for i in range(n):
    units=int(input())
    total+=units
    if units>10:
        count+=1
print("Total Units:",total)
print("Days Above 10:",count)

# Q66. Shopping Bill Analyzer
n=int(input())
total=0
count=0
for i in range(n):
    price=int(input())
    total+=price
    if price>1000:
        count+=1
print("Total Bill:",total)
print("Products Above 1000:",count)

# Q67. Login Attempt Analyzer
n=int(input())
successful=0
failed=0
for i in range(n):
    attempt=input()
    if attempt=="success":
        successful+=1
    elif attempt=="failed":
        failed+=1
print("Successful:",successful)
print("Failed:",failed)
print(f"Success Rate: {successful/n*100:.1f}%")