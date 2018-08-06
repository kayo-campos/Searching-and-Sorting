import matplotlib.pyplot as plt
import random
import timeit

from Selection_Sort.SelectionSort import selectionSort
## Edit line above to include the desired sorting function
## OBS - Make sure the folder containing the sorting function
## has a __init__.py, so python understand it as a package


 def drawGraphic(x, y, z, xl="Entradas", yl="Saídas"):
     plt.plot(x, y, label="Caso médio")
     plt.plot(x, z, label="Pior caso")
     plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
     plt.ylabel(yl)
     plt.xlabel(xl)
     plt.show()

def generateRandomList(size):
    random_list = []
    while len(random_list) < size:
        n = random.randint(1, size)
        random_list.append(n)
    return random_list

def generateDecreasingList(size):
    decreasing_list = [i for i in range(size, -1, -1)]
    return decreasing_list

def timeToSort(sorting_method, list_generating_method, list_size):
    list_to_sort = list_generating_method(list_size)
    print('Calculando para ' + str(list_size))
    time = timeit.timeit(sorting_method + "({})".format(list_to_sort), setup="from __main__ import " + sorting_method,
                         number=1)
    print('Tempo necessário: ' + str(time))

    return time
        
if __name__ == '__main__':
    ## Edit value of sorting_method so it can be correctly passed
    ## as argument to timeToSort function
    ## OBS - Make sure you write it the same way as you wrote the
    ## function name in its package
    sorting_method = "selectionSort"
    numbers_to_generate = [1000, 10000, 20000, 30000, 40000, 50000, 100000]
    time_to_generate_medium_case = [timeToSort(sorting_method, generateRandomList, size) for size in numbers_to_generate]
    time_to_generate_worst_case = [timeToSort(sorting_method, generateDecreasingList, size) for size in numbers_to_generate]

    drawGraphic(numbers_to_generate, time_to_generate_medium_case, time_to_generate_worst_case, "Tamanho do array para ordenar", "Tempo")

