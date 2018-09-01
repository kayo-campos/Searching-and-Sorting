def shellSort(array):
  # Uncomment commented lines to count operations performed by the algorithm
  # operations_count = 0
  gap = len(array) // 2
  while gap:
    for i, el in enumerate(array):
      while i >= gap and array[i - gap] > el:
        array[i] = array[i - gap]
        i -= gap
        # operations_count += 1
      array[i] = el
    if gap == 2:
      gap = 1
    else:
      gap //= 2
  # return operations_count
  return array


array = [1,4,6,2,4,6,3,2,2,4,5,6,1,223,3,2,1,24,1,23,12,31,23,1,1]
print(shellSort(array))