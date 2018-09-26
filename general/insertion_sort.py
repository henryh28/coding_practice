def insertionSort(array):
  for index in range(len(array)):
    sorting_value = array[index]
    position = index

    while position > 0 and array[position - 1] > sorting_value:
      array[position] = array[position - 1]
      position -= 1

    array[position] = sorting_value
    