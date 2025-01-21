def password_checker():
    pswrd = input("Enter your password: ")
    if len(pswrd) < 8:
        print("Password is too short")
    elif not any (char.isupper() for char in pswrd):
        print("Password must contain an uppercase letter")
    else:
        print("Password is strong")
password_checker()