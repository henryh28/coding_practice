def breakingRecords(scores):
    max_min = [0, 0]
    low = high = scores[0]

    for i in range(1, len(scores)):
        if scores[i] > high:
            high = scores[i]
            max_min[0] += 1
        elif scores[i] < low:
            low = scores[i]
            max_min[1] += 1
      
    return(max_min)
    