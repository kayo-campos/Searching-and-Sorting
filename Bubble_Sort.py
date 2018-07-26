def bubbleSort(list):
  for i in range(len(list) - 1, 0 , -1):
    for j in range(i):
      if list[j] > list[j + 1]:
        aux = list[j]
        list[j] = list[j + 1]
        list[j + 1] = aux
  return list

unordered_list = [23, 42, 8, 16, 15, 4]

ordered_list = bubbleSort(unordered_list)

print(ordered_list)