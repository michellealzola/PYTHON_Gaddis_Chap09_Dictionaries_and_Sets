def get_set(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip('\n').rstrip('.')

    text_set = set()
    for line in lines:
        words = line.split(' ')
        for word in words:
            text_set.add(word.strip(','))

    return text_set


def get_unique_words(file1, file2):
    print('List of all the unique words contained in both files')
    print('----------------------------------------------------')
    file = file1.union(file2)
    for word in file:
        print(word)
    print()


def get_words_on_both_files(file1, file2):
    print('List of the words that appear in both files')
    print('----------------------------------------------------')
    file = file1.intersection(file2)
    for word in file:
        print(word)
    print()


def get_words_on_file1_not_on_file2(file1, file2):
    print('List of the words that appear in the first file but not the second')
    print('----------------------------------------------------')
    file = file1.difference(file2)
    for word in file:
        print(word)
    print()


def get_words_on_file2_not_on_file1(file1, file2):
    print('List of the words that appear in the second file but not the first')
    print('----------------------------------------------------')
    file = file2.difference(file1)
    for word in file:
        print(word)
    print()


def get_words_not_on_both_files(file1, file2):
    print('List of the words that appear in either the first or second file, but not both')
    print('----------------------------------------------------')
    file = file1.symmetric_difference(file2)
    for word in file:
        print(word)
    print()


def main():
    infile1 = open('text1.txt', 'r')
    infile2 = open('text2.txt', 'r')

    lines1 = infile1.readlines()
    lines2 = infile2.readlines()

    file1 = get_set(lines1)
    file2 = get_set(lines2)

    get_unique_words(file1, file2)
    get_words_on_both_files(file1, file2)
    get_words_on_file1_not_on_file2(file1, file2)
    get_words_on_file2_not_on_file1(file1, file2)
    get_words_not_on_both_files(file1, file2)


if __name__ == '__main__':
    main()
