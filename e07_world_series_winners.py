def main():
    infile = open('WorldSeriesWinners.txt', 'r')
    winners = infile.readlines()
    for i in range(len(winners)):
        winners[i] = winners[i].rstrip('\n')
    winners_dict = {}
    year = 1903
    for w in range(len(winners)):
        winners_dict[(year + w)] = winners[w]

    search = int(input('Enter a year from 1903 to 2008: '))

    winner = winners_dict.get(search)

    print(f'The winner for the year {search} is {winner}')

    winner_for_year_list = []
    for value in winners_dict:
        if winner == winners_dict.get(value):
            winner_for_year_list.append(winner)
    print(f'The {winner} won the World series {len(winner_for_year_list)} times')


if __name__ == '__main__':
    main()
