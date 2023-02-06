room_numbers = {'CS101': '3004',
                'CS102': '4501',
                'CS103': '6755',
                'NT110': '1244',
                'CM241': '1411'}

instructors = {'CS101': 'Haynes',
               'CS102': 'Alvarado',
               'CS103': 'Rich',
               'NT110': 'Burke',
               'CM241': 'Lee'}

meeting_times = {'CS101': '8:00 a.m.',
                 'CS102': '9:00 a.m.',
                 'CS103': '10:00 a.m.',
                 'NT110': '11:00 a.m.',
                 'CM241': '1:00 ap.m.'}


def get_room_number(search):
    if search in room_numbers:
        print('The room number is: ', room_numbers[search])
    else:
        print('Room number not found.')


def get_instructor(search):
    if search in instructors:
        print('The instructor is: ', instructors[search])
    else:
        print('Instructor not found.')


def get_meeting_time(search):
    if search in meeting_times:
        print('The meeting time is: ', meeting_times[search])
    else:
        print('Meeting time not found.')


def main():
    search = input('Enter course number: ')
    get_room_number(search)
    get_instructor(search)
    get_meeting_time(search)


if __name__ == '__main__':
    main()
