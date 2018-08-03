def insertionSort(list_to_sort):
  size = len(list_to_sort)
  for i in range(1, size):
    if list_to_sort[i] < list_to_sort[i - 1]:
      unsorted_element = list_to_sort[i]
      j = i
      while list_to_sort[j - 1] > unsorted_element and j > 0:
        list_to_sort[j] = list_to_sort[j - 1]
        j = j - 1
      list_to_sort[j] = unsorted_element
  print(list_to_sort)