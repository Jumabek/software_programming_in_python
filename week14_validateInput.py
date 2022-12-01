def read_input_with_validation():
    while True:
        print('Enter your age:')
        age = input() # twenty
        if age.isdecimal(): # age.isdecimal()=>False
            break  
        print('Please enter a number for your age.')

    while True:
        print('Select a new password (letters and numbers only):')
        password = input()
        if password.isalnum():
            break
        print('Passwords can only have letters and numbers.')

if __name__ == '__main__':
    print("__name__",__name__) 
    read_input_with_validation()
