def partition(array, initial_position, final_position):
  pivot = array[final_position]
  checking_position = initial_position - 1

  for loop_controller in range(initial_position, final_position):
    if array[loop_controller] <= pivot:
      checking_position += 1
      array[checking_position], array[loop_controller] = array[loop_controller], array[checking_position]
  array[checking_position + 1], array[final_position] = array[final_position], array[checking_position + 1]
  return checking_position + 1

def quickSort(array, initial_position, final_position):
  if initial_position < final_position:
    p = partition(array, initial_position, final_position)
    quickSort(array, initial_position, p - 1)
    quickSort(array, p + 1, final_position)
  return array