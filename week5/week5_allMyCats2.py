catNames = [] # [] creates empty list
while True: # this runs all the time
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    #catNames = catNames + [name]  # list concatenation
    catNames +=  [name]
print('The cat names are:')
for name in catNames:
    print('  ' + name)