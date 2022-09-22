print("enter your age")
try:
    string_age = input()
    my_age = int(string_age)
except Exception as e:
    print("Exception ", e, 'has occurred')
    print("You entered wrong type, pls enter integer")
    string_age = input()
    my_age = int(string_age)
    
print("You will ", my_age+10, 'years old after 10 years' )

