contacts = {}

running = True;

while running:
    command = input('enter A(dd) D(elete) F(ind) Q(uit)')
    if command == 'A' or command == 'a':
        name = input('enter a new name');
        print('enter a phone number for', name, end=':')
        number=input()
        contacts[name] = number
    elif command == 'D' or command == 'd':
        name = input('enter name to delete')
        del contacts[name]
    elif command == 'F' or command == 'f':
        name = input('enter a name to search for')
        print(name,contacts[name],sep=':')
    elif command == 'Q' or command == 'q':
        running = False
    elif command == 'list':
        print(contacts)
    else:
        print(command, 'is not a valid command')

