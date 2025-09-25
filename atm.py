while True:
    correct_password=1112
    password=int(input("Enter your password:"))
    if password==correct_password:
        print("Valid Password")
        break
    else:
        print("Your Password is Wrong\n")