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
      gap = int(gap * 5.0 / 11)
  # return operations_count
  return array