def mergeSort(unsorted_list):
  size = len(unsorted_list)
  if size > 1:
    mid = size // 2
    left_half = unsorted_list[:mid]
    right_half = unsorted_list[mid:]

    mergeSort(left_half)
    mergeSort(right_half)

    left_size = len(left_half)
    right_size = len(right_half)

    i, j, k = 0, 0, 0

    while i < left_size and j < right_size:
      if left_half[i] < right_half[j]:
        unsorted_list[k] = left_half[i]
        i += 1
      else:
        unsorted_list[k] = right_half[j]
        j = j + 1
      k += 1

    while i < len(left_half):
      unsorted_list[k]=left_half[i]
      i=i+1
      k=k+1

    while j < len(right_half):
      unsorted_list[k]=right_half[j]
      j=j+1
      k=k+1
