name = str(input('What is your name? '))
if name == 'Diogo':
    print('What a wonderful name, huh?? ')
elif name == 'Pedro' or name == 'Maria' or name == 'Paulo':
    print('Your name is very popular in Brazil')
else:
    print('Your name is so normal')
print('Have a good day, {}!'.format(name))