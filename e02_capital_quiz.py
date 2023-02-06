import random


def main():
    infile = open('list_national_capitals.csv', 'r')
    lines = infile.readlines()
    infile.close()

    for i in range(len(lines)):
        lines[i] = lines[i].rstrip('\n').strip('\xa0')

    capital_dict = {}
    countries = []
    for line in lines:
        token = line.split(',')

        capital_dict[token[0]] = token[1]
        countries.append(token[0])

    count_correct = 0
    count_total_quiz = 0
    again = 'y'
    while again == 'y' or again == 'Y':
        random_country = random.choice(countries)
        search = input(f'What is the capital of {random_country}? ')

        if search == capital_dict[random_country]:
            print('You are correct')
            count_correct += 1
            count_total_quiz += 1
            again = input('Play again? y/n: ')
        else:
            print('That is incorrect')
            count_total_quiz += 1
            again = input('Play again? y/n: ')

    print(f'Total correct answers: {count_correct}')
    print(f'Total number of plays: {count_total_quiz}')
    average = count_correct / count_total_quiz * 100
    print(f'Your average is: {average}%')


if __name__ == '__main__':
    main()
