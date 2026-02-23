student_name=input("Enter Student Name:")
student_age=int(input("Enter Age:"))
student_percentage=float(input("Enter Percentage:"))
student_family_income=float(input("Enter Family Income:"))
student_rural=input("Is student from rural?:(True or False):")=="True"
eligible=(student_percentage>90) or (student_percentage>85 and student_family_income<300000)
print("\nStudent details")
print("Name:", student_name)
print("Age:",student_age)
print("Percentage:",student_percentage)
print("Family income:",student_family_income)
print("Rural area:",student_rural)
if eligible:
    print("Eligible for scholarship")
else:
    print("Not eligible")