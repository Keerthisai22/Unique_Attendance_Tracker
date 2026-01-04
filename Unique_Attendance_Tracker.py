attendance=set()
n=int(input("Enter the number of students="))
for i in range(n):
    roll=int(input(f"Enter the roll number{i+1}="))
    attendance.add(roll)
print("\n----------Unique Attendance Tracker-----------\n")
print("Number of present students=",len(attendance))
print("present students=",attendance)
