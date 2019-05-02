def mix(s1, s2):
    letters, answer, uniques = {}, [], set()
    
    for char in set(s1 + s2):
        if char.islower() == True:
            uniques.add(char)
            letters[char] = [0, 0]

    for x in s1:
        if x in letters:
            letters[x][0] += 1
    for y in s2:
        if y in letters:
            letters[y][1] += 1

    for unique in uniques:
        if letters[unique][0] > 1 or letters[unique][1] > 1:
            if letters[unique][0] > letters[unique][1]:
                answer.append("1:{}".format(unique * letters[unique][0]))
            elif letters[unique][1] > letters[unique][0]:
                answer.append("2:{}".format(unique * letters[unique][1]))
            elif letters[unique][1] == letters[unique][0]:
                answer.append("=:{}".format(unique * letters[unique][0]))
        
    answer.sort(key=lambda k: (-len(k), k))
    return ("/".join(answer) if answer else "")
    
