def primes_below(limit):
  sieve = [0] * (limit + 1)
  answers = []
#  totals = 0

  for number in range(3, limit + 1, 2):
    # unmarked number, will be a prime number
    if sieve[number] == 0:
      answers.append(number)
      sieve[number] = 1
#      totals += 1

      multiple_of = number
      for multiple_of in range(number ** 2, limit + 1, number):
#        totals += 1 
        sieve[multiple_of] = 1
        multiple_of += number

#  print("total calc: ", totals)
  return (sum(answers) + 2)


print(primes_below(2000000))

#                                no opt       num/3  square root      sieve
# for 1000:           76127:     14,622       6,522        1,970      1,079
# for 10000:        5736396:    766,633     305,875       34,983     13,210
# for 50000:      121013308: 13,262,249   5,076,709      268,722     73,409
# for 100000:     454396537: 46,214,479  17,463,013      654,029    152,670
# for 1000000:  37550402023:                          13,005,901  1,700,546
# for 2000000: 142913828922:                          32,467,511  3,496,711
