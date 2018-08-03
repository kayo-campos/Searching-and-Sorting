def insertionSort(array):
  size = len(array)
  for i in range(1, size):
    if array[i] < array[i - 1]:
      unsorted_element = array[i]
      j = i
      while array[j - 1] > unsorted_element and j > 0:
        array[j] = array[j - 1]
        j = j - 1
      array[j] = unsorted_element
  return array
  