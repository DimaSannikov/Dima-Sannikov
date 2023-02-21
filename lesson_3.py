list_ = [2, 6, 16, 1, 4, 11, 3, 14]


def find_second_max_1(array):
    index = 0
    max_element = 0
    secondMax = 0

    while index < len(array):
        if array[index] > max_element:
            max_element = array[index]
        if array[index] < max_element:
            secondMax = array[index]

        index += 1
    print(secondMax)


def find_second_max_2(array):

    current_index = 0
    max_number_index = 0
    max_ = array[0]

    while current_index < len(array):
        if array[current_index] > max_:
            max_ = array[current_index]
            max_number_index = current_index

        current_index += 1
    # print(max_number_index, max_)

    current_index = 0
    second_max = array[0]
    if max_number_index == 0:
        second_max = array[1]
    while current_index < len(array):
        if array[current_index] > second_max and current_index != max_number_index:
            second_max = array[current_index]

        current_index += 1
    print(second_max)


def find_second_max_3(array):
    size = len(array)
    first_max = array[0]
    second_max = array[0]

    if array[1] > first_max:
        first_max = array[1]
    else:
        second_max = array[1]

    index = 2

    while index < size:
        if array[index] > first_max:
            second_max = first_max
            first_max = array[index]
        else:
            if array[index] > second_max:
                second_max = array[index]
        index += 1

    print(second_max)


find_second_max_1(list_)
find_second_max_2(list_)
find_second_max_3(list_)
