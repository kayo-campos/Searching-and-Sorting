#import matplotlib.pyplot as plt
import random
import timeit
import threading

from Selection_Sort.SelectionSort import selectionSort
## Edit line above to include the desired sorting function
## OBS - Make sure the folder containing the sorting function
## has a __init__.py, so python understands it as a package


#  def drawGraphic(x, y, z, xl="Entradas", yl="Saídas"):
#      plt.plot(x, y, label="Caso médio")
#      plt.plot(x, z, label="Pior caso")
#      plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
#      plt.ylabel(yl)
#      plt.xlabel(xl)
#      plt.show()

class CalculationThread (threading.Thread):
    def __init__(self, threadID, name, sorting_method, list_generating_method, numbers_to_generate):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.sorting_method = sorting_method
        self.list_generating_method = list_generating_method
        self.numbers_to_generate = numbers_to_generate
        self.results = []

    def run(self):
        time_to_generate = [timeToSort(self.sorting_method, self.list_generating_method, size) for size in self.numbers_to_generate]
        return time_to_generate
        

def generateRandomList(size):
    random_list = []
    actual_length = 0
    while actual_length < size:
        n = random.randint(1, size)
        random_list.append(n)
        actual_length += 1
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
    ## OBS - Make sure you write exact the same as you wrote the
    ## function name in its package
    sorting_method = "selectionSort"
    numbers_to_generate = [1000, 10000, 20000, 30000, 40000, 50000, 100000]
    medium_case_thread = CalculationThread(1, 'Medium Case', sorting_method, generateRandomList, numbers_to_generate)
    worst_case_thread = CalculationThread(2, 'Worst Case', sorting_method, generateRandomList, numbers_to_generate)
    
    variable = medium_case_thread.start()
    worst_case_thread.start()
    #drawGraphic(numbers_to_generate, time_to_generate_medium_case, time_to_generate_worst_case, "Tamanho do array para ordenar", "Tempo")

