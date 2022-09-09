def first_duplicate_finder(int_list):
    '''
    :param int_list: From a loop defined on the Global scope the objetive was to verify the numbers one by one and
    verify the occurrences of duplicates.
    :return: The duplicates found or (-1) if none found.
    '''

    verified_numbers = set()
    first_duplicate = -1

    for number in int_list:
        if number in verified_numbers:
            first_duplicate = number
            break

        verified_numbers.add(number)

    return first_duplicate


integers_list = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

if __name__ == '__main__':
    for int_lists in integers_list:
        print(int_lists, first_duplicate_finder(int_lists))
