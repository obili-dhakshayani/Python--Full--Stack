name=input("Enter your name :").lower()
mid_marks=int(input("Enter your mid marks :"))
attendance=int(input("Enter your attendance :"))
fees_details=input("Are you fees paid ?:").lower()
if (name == "rudra" and mid_marks >= 25 and attendance >=75 and fees_details == "paid"):
    print("Eligible for External exams")
else:
    print("not Eligible for External exams")