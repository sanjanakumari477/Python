Name = input("enter any name: ")
Dob = input("enter Dob: ")
Roll_no = int(input("enter Roll no: "))

print("----Marksheet----")

sub1 = int(input("enter marks of Maths : "))
sub2 = int(input("enter marks of Sst : "))
sub3 = int(input("enter marks of Science : "))
sub4 = int(input("enter marks of Hindi : "))
sub5 = int(input("enter marks Sanskrit : "))

Tot = sub1 + sub2 + sub3 + sub4 + sub5
percentage = Tot / 5

print("Name:", Name)
print("DOB:", Dob)
print("Roll No:", Roll_no)
print("Total Marks:", Tot)
print("Percentage:", percentage)

if percentage >= 80:
    print("Excellent")

elif percentage >= 60:
    print("Very Good")

elif percentage >= 40:
    print("Good")

else:
    print("Poor")
