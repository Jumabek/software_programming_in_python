# following three global variables are used throught the program
students = [
    'Josue Sutton'
    , 'Josephine Graham'
    , 'Jesus Moss'
    , 'Kian Crane'
    ,'Presley Cooper'
    ,'Jaeden Yu'
    ,'LorenzoptionLawrence'
    ,'Lindsey Mcdonald'
    ,'Grace Rivers'
    ,'Lawrence Giles'
    ,'Blake Odonnell'
    ,'Alexis Bruce'
]
questions_asked = [0]*len(students) # makes a list with length of students, and fills it with 0
correct_answers = [0]*len(students) # makes a list with length of students, and fills it with 0


def print_user_options():
    print("Select option for performing an operation:\n")
    print("pa - print all students")
    print("a - ask a question")
    print("p - print the performance of the students")
    print("q - quit")
    option = input("enter here: ")
    return option


def print_all_students():
    print("All students:")
    for i, student in enumerate(students):
        print(i, student)


def get_random_student():
    import random
    return random.choice(students)


def ask_question():
    '''
        1. selects a random student
        2. records whether answer is correct
    '''
    selected_student = get_random_student()
    print("Selected student: ", selected_student)

    print("Now teacher asks the question...")
    input("press enter to record students response...") # used for pausing
    
    print("is the answer correct teacher?")
    teacher_input = input("enter 'Y' or 'N': ")
    if teacher_input not in ['Y','N']:
        print("Invalid input")
        return # incase of invalid input, we don't want to continue

    # now we get the student index, then update his performance
    I = students.index(selected_student)
    questions_asked[I] += 1 # add 1 to the number of questions asked
    if teacher_input == 'Y':
        correct_answers[I] += 1 # add 1 to the number of correct answers
    print("Student answer is recorded!")


def print_performance():
    print("***Performance:***")
    for i, student in enumerate(students):
        if questions_asked[i]> 0:
            print(student, ":", correct_answers[i], "/", questions_asked[i])


print("Welcome to the Student Questioner App")
print("This app will help you to ask questions to students randomly and keep their progress")
print("Let's get started")
while True:
    try: # ensures loops keeps running even if there is an error
        print("-----------------------------")
        option= print_user_options()
        print('You selected option: ', option)
        print()

        if option== 'p':
            print_performance()
        elif option== 'pa':
            print_all_students()
        elif option== 'a':
            ask_question() # this function will ask a question from randomly selected student and record the answer
        elif option=='q':
            print("Quitting")
            break
        else:
            print("Invalid option")
        
        print('\n\n')
        input("press any key to continue")# this pauses the program until user presses any key to continue

    except BaseException as e:
        print("Exception occurred. But program keeps running")
        