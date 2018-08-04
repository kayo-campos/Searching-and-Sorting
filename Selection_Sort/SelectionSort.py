import matplotlib.pyplot as plt
import random
import timeit


def drawGraphic(x, y, z, xl="Entradas", yl="Saídas"):
    plt.plot(x, y, label="Caso médio")
    plt.plot(x, z, label="Pior caso")
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()


def generateRandomList(tam):
    random_list = []
    while len(random_list) != tam:
        n = random.randint(1, tam)
        random_list.append(n)
    return random_list


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


def timeToSortMediumCase(size):
    list_to_sort = generateRandomList(size)
    print("**CASO MÉDIO**")
    print('calculando para ' + str(size))
    time = timeit.timeit("selectionSort({})".format(list_to_sort), setup="from __main__ import selectionSort",
                         number=1)
    print('tempo necessário: ' + str(time))

    return time

def timeToSortWorstCase(size):
    list_to_sort = [i for i in range(size, 0, -1)]

    print("**PIOR CASO**")
    print('calculando para ' + str(size))
    time = timeit.timeit("selectionSort({})".format(list_to_sort), setup="from __main__ import selectionSort",
                         number=1)
    print('tempo necessário: ' + str(time))

    return time

numbers_to_generate = [1000, 10000, 20000, 30000, 40000, 50000, 100000]
time_to_generate_medium_case = [timeToSortMediumCase(quantity) for quantity in numbers_to_generate]
time_to_generate_worst_case = [timeToSortWorstCase(quantity) for quantity in numbers_to_generate]

drawGraphic(numbers_to_generate, time_to_generate_medium_case, time_to_generate_worst_case, "Tamanho do array para ordenar", "Tempo")

