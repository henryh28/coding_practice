#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

def answer(n):
  primes = [2, 3]
  answer = primes

  if n == 1:
    return primes[0]
  elif n == 2:
    return primes[1]

  # do n - 2 times (minimum n of 3 would be done once)
  for i in range(n - 2):
    # start at last prime + 2, 5 to start
    start = primes[-1]
    # making duplicate list because can't iterate over changing list
    prime_dupe = list(primes)[1:]
    added = False

    while added == False:
      start += 2
      for test in prime_dupe:
        if start % test == 0:
          break

        if test == prime_dupe[-1]:
          primes.append(start)
          added = True

  print(primes)
print (answer(10001))
