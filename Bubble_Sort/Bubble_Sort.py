def bubbleSort(array):
  size = len(array)
  for i in range(size - 1, 0 , -1):
    for j in range(i):
      if array[j] > array[j + 1]:
        aux = array[j]
        array[j] = array[j + 1]
        array[j + 1] = aux
  return array

