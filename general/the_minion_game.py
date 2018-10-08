def minion_game(string):
  vowels = ['A', 'E', 'I', 'O', 'U']
  stu_score, kev_score = 0, 0

  # Stuart starts with consonants, Kevin starts with vowels
  for index in range(len(string)):
    if string[index] not in vowels:
      stu_score += len(string) - index
    else:
      kev_score += len(string) - index

  if stu_score > kev_score:
    print("Stuart", stu_score)
  elif kev_score > stu_score:
    print("Kevin", kev_score)
  else:
    print("Draw")
