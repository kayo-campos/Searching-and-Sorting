def selectionSort(array):
    size = len(array)

    for base_position in range(size):
        lowest_number_position = base_position
        for check_position in range(base_position + 1, size):
            if array[check_position] < array[lowest_number_position]:
                lowest_number_position = check_position
        aux = array[base_position]
        array[base_position] = array[lowest_number_position]
        array[lowest_number_position] = aux
    return array
