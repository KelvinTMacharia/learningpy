StudentsName = input("The name of the student is: ")
English = int(input("Enter English marks in percentage: "))
Kiswahili = int(input("Enter Kiswahili marks in percentage: "))
Mathematics = int(input("Enter Mathematics marks in percentage: "))
Science = int(input("Enter Science marks in percentage: "))
SocialStudies = int(input("Enter SocialStudies marks in percentage: "))
def marks():
    if English <= 0:
        print("Check the English subject")
    elif Kiswahili <= 0:
        print("check the Kiswahili subject")
    elif Mathematics <= 0:
        print("check the Mathematics subject")
    elif Science <= 0:
        print("check the Science subject")
    elif SocialStudies <= 0:
        print("check the Social Studies subject")
    else:
        print(English + Kiswahili + Mathematics + Science + SocialStudies)
        TotalMarks = English + Kiswahili + Mathematics + Science + SocialStudies
    return TotalMarks


AvgMarks = marks()/5
print(AvgMarks)
if 79 <= AvgMarks < 100:
    print(StudentsName + " has a Grade A")
elif 78 >= AvgMarks >= 60:
    print(StudentsName + " has a Grade B")
elif 59 >= AvgMarks >= 50:
    print(StudentsName + " has a Grade C")
elif 49 >= AvgMarks >= 40:
    print(StudentsName + " has a Grade D")
elif AvgMarks < 40:
    print(StudentsName + " has a Grade E")
else:
    print("invalid")