# Complete the getSortedList function below.
def getSortedList(names):
  from collections import defaultdict

  answer = []
  name_set = []
  name_dict = defaultdict(list)
  roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX", "XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI", "XXXVII", "XXXVIII", "XXXIX", "XL",  "XLI", "XLII", "XLIII", "XLIV", "XLV", "XLVI", "XLVII", "XLVIII", "XLIX", "L"] 

  for name in names:
    name_split = name.split()
    name_dict[name_split[0]].append(name_split[1])

  for key, value in name_dict.items():
    # sorted_num contains sorted tuples of the roman numer portion
    sorted_num = []
    for number in value:
      sorted_num.append((roman.index(number), number))
      
    sorted_num.sort()
    name_dict[key] = sorted_num
    name_set.append(key)

  name_set.sort()
  for name in name_set:
    for index in range(len(name_dict[name])):
      answer.append(name +  " " + name_dict[name][index][1])

  return (answer)

test_1 = ["Louis IX", "Phillipe II"]
print (getSortedList(test_1))

test_2 = ["Louis IX", "Louis VIII"]
print (getSortedList(test_2))

test_3 = ["Philip II", "Phillipe II"]
print (getSortedList(test_3))
