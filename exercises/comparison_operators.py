name = input('Input a name:')

if len(name) < 3:
    print('name must be at least 3 characters'.title()) 
elif len(name) > 50:
    print('name can be a maximum of 50 characters'.title())
else:
    print('name looks good!'.title())