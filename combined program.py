name=input("Enter your name :")
python_marks=float(input("Enter python marks :"))
java_marks=float(input("Enter java marks :"))
attendance_percentage=int(input("Enter your attendance percentage :"))
is_project_allowed=input("is project is allowed :").lower()
sum=python_marks + java_marks
Average_percentage=sum/2
print(Average_percentage >=50 and attendance_percentage >=75 and is_project_allowed)