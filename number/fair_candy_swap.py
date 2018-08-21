def fairCandySwap(self, A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: List[int]
    """
    sum_a = sum(A)
    sum_b = sum(B)
    unique = set(B)
    target = (sum_a + sum_b) // 2

    for number in A:
        need = target - (sum_a - number)
      
        if need in unique:
            return ([number, need])
        