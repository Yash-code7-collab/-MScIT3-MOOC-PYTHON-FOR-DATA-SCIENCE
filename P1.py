

# Student Information
roll_no = (input("Enter your Roll No : "))
name = input("Enter your Name : ")
age = int(input("Enter your Age : "))


maths = int(input("Enter your Maths Mark : "))
science = int(input("Enter your Science Mark : "))
english = int(input("Enter your English Mark : "))
computer = int(input("Enter your computer Mark : "))
gujarati = int(input("Enter your Gujarati Mark : "))


total_marks = maths + science + english + computer + gujarati

# Calculate percentage
percentage = total_marks / 5



passed = (
    maths >= 40 and
    science >= 40 and
    english >= 40 and
    computer >= 40 and
    gujarati >= 40
)


print("========== Student Report ==========")
print(f"Roll No.   : {roll_no}")
print(f"Name       : {name}")
print(f"Age        : {age}")

print("\nMarks")
print(f"Maths      : {maths}")
print(f"Science    : {science}")
print(f"English    : {english}")
print(f"Computer   : {computer}")
print(f"Gujarati   : {gujarati}")

print("\nTotal Marks :", total_marks)
print(f"Percentage  : {percentage:.2f}%")

# Display Result
if passed:
    print("Result      : PASS")
else:
    print("Result      : FAIL")