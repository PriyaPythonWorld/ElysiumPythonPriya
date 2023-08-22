marks = int(input("Enter your marks: "))
if marks > 100:
    print("Warning: Enter value below 100")
elif marks >= 90 and marks <= 100:
    print("Outstanding, your Grade is A+")
elif marks >= 80 and marks < 90:
    print("Excellant, your Grade is A")
elif marks >= 70 and marks < 80:
    print("Very good, your Grade is B")
elif marks >= 60 and marks < 70:
    print("Good, your Grade is C")
elif marks >= 50 and marks < 60:
    print("Above average, your Grade is D")
elif marks >= 40 and marks < 50:
    print("Average, your Grade is E")
elif marks >= 0 and marks < 40:
    print("Fail")
else:
    print("Enter valid number")