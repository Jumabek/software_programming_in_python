# get currnet datetime
import datetime
import pyperclip

while True:
    cdt = datetime.datetime.now()
    # put this to clipboard
    pyperclip.copy(cdt.__str__())

