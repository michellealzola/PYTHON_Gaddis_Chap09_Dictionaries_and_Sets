def main():
    infile = open('Kennedy.txt', 'r')
    lines = infile.readlines()
    infile.close()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip('\n')

    kennedy_words = set()
    for line in lines:
        words = line.split(' ')
        for word in words:
            kennedy_words.add(word)

    print('The unique words in the file are: ')
    print('---------------------------------')
    for k_word in kennedy_words:
        print(k_word)


if __name__ == '__main__':
    main()
