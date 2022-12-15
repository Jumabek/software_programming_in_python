import webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
    print(f"adress you passed is: {address}")
    webbrowser.open('https://www.google.com/maps/place/' + address)