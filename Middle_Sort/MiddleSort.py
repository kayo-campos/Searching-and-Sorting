def middleSort(arr):
  new_arr = []
  while len(arr) > 0:
    lowest = 0
    highest = 0
    for i in range(len(arr)):
      if arr[i] < arr[lowest]:
        lowest = i
      elif arr[i] > arr[highest]:
        highest = i
    
    middle = len(new_arr) // 2
    new_arr.insert(middle, arr.pop(highest))

    if lowest != highest:
      if lowest > highest:
        lowest -= 1
      new_arr.insert(middle, arr.pop(lowest))
  
  return new_arr