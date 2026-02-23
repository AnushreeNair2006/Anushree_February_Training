correct_username="AdminSystem"
correct_password="pass12"
active_status=True
username=input("Enter username:")
password=input("Enter password:")
if username == correct_username and password == correct_password and active_status:
    print("Login Successful")
elif username == correct_username and password == correct_password and not active_status:
    print("Account Disabled")
else:
    print("Wrong Credentials")