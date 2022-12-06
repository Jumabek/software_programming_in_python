import time

indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.

        # indent variable increases until 20,. then goes down until 0
        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False
        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except BaseException as e: # base exception contains inside KeyboardInterrupt error
    print('error message',repr(e)) # https://stackoverflow.com/questions/1483429/how-do-i-print-an-exception-in-python
    print("thanks for running`")