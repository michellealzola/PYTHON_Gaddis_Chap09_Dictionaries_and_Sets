import pickle

menus = {1: 'Look up email address',
         2: 'Add a new name and email address',
         3: 'Change an existing email address',
         4: 'Delete an existing name and email address',
         0: 'Quit'}

end_of_file = False
input_file = open('email_records.dat', 'rb')
while not end_of_file:
    try:
        emails = pickle.load(input_file)
    except EOFError:
        end_of_file = True
input_file.close()


def get_menu():
    print('Select from menu:')
    print('-------------------------------')
    for k, v in menus.items():
        print(f'{k}: {v}')


def look_up(emails):
    search = input('Enter email: ')
    for k, v in emails.items():
        if search == v:
            print(f'Name: {k}\nEmail: {v}')


def add_new(emails):
    outfile = open('email_records.dat', 'wb')
    name = input('Enter name: ')
    email = input('Enter email: ')
    if name in emails:
        print('Name already exists.')
    else:
        emails[name] = email
    pickle.dump(emails, outfile)
    outfile.close()
    print('New record added')
    print(emails)


def change_email(emails):
    name = input('Enter name: ')
    if name not in emails:
        print('That name is not found.')
    else:
        email = input('Enter a new email: ')
        emails[name] = email
    print('New record added')
    print(emails)


def delete_record(emails):
    name = input('Enter name: ')
    if name not in emails:
        print('That name is not found.')
    else:
        del emails[name]
    print('Record deleted')
    print(emails)


def main():
    get_menu()
    selection = int(input('Enter your selection: '))
    while selection != 0:
        if selection == 1:
            look_up(emails)
        elif selection == 2:
            add_new(emails)
        elif selection == 3:
            change_email(emails)
        else:
            delete_record(emails)
        get_menu()
        selection = int(input('Enter your selection: '))

    print('Thank you for using the App')


if __name__ == '__main__':
    main()
