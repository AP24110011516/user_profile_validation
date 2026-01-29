Name = str(input("Enter your name: "))
Email = str(input("Enter your email: "))
Mobile = (input("Enter your mobile number: "))
Age = int(input("Enter your age: "))

if Name.count(" ") >=1:
    if Name[0]!=" ":
        if Name[len(Name)-1] !=" ":
           Name_valid = True
        else:
            Name_valid = False
    else:
        Name_valid = False
else:
    Name_valid = False

if'@' in Email and '.' in Email and Email[0]!='@':
    Email_valid = True
else:
    Email_valid = False


if len(Mobile) == 10 and Mobile.isdigit() and Mobile[0]!='0':
    Mobile_valid = True
else:
    Mobile_valid = False

if Age>=18 and Age<=60:
    Age_valid = True
else:
    Age_valid = False
if Name_valid and Mobile_valid and Age_valid:
    print("user profile is VAILD")
else:
    print("user profile is NOT VAILD")

