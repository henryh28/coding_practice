def answer(input):
  balances = {}
  answer =  []

  for line in input:
    if line[:3] == "API":
      # Get total amount of transaction
      amount_start = line.find("amount=")
      amount_end = line.find("&merchant=")
      amount = int(line[amount_start + 7 : amount_end])
      stripe_cut = int(amount * 0.029) + 30

      # find merchant key
      merchant_id_start = line.find("&merchant=")

      # Merchant + Destination account
      if line.find("destination[account]") != -1:
        merchant_id_end = line.find("&destination[account]")
        dest_id_end = line.find("&destination[amount]")

        merchant_key = line[merchant_id_start + 10: merchant_id_end]
        dest_key = line[merchant_id_end + 22:dest_id_end]
        dest_amount = int(line[dest_id_end + 21:])

        # Check if merchant key is in balances
        if merchant_key not in balances:
          balances[merchant_key] = 0

        if dest_key not in balances:
          balances[dest_key] = 0
        
        # Deposit to merchant and destination accounts
        balances[merchant_key] += amount - stripe_cut - dest_amount
        balances[dest_key] += dest_amount

      else: # Only Merchant
        merchant_key = line[merchant_id_start + 10:]

        if merchant_key not in balances:
          balances[merchant_key] = 0
        
        # Deposit to merchant account
        balances[merchant_key] += amount - stripe_cut

    elif line[:3] == "BAL":  # Add result of balance inquiry to answer
      merchant_id_start = line.find("&merchant=")
      merchant_id = line[merchant_id_start + 15:]

      answer.append(balances[merchant_id])

  print("final balance: ", balances)

  return (answer)


print("\n =============== test case # 1 ===================")

# [64, 877]
input_1 = ["API: amount=1000&merchant=123456789&destination[account]=111111&destination[amount]=877", "BAL: merchant=123456789", "BAL: merchant=111111"]

print(answer(input_1))

print("\n =============== test case # 2 ===================")

# [1912]
input_2 = ["API: amount=2000&merchant=10101010", "BAL: merchant=10101010"]

print(answer(input_2))

print("\n =============== test case # 3 ===================")

# [167, 877]
input_3 = ["API: amount=1000&merchant=123456789&destination[account]=111111&destination[amount]=877", "API: amount=800&merchant=123456789&destination[account]=112211&destination[amount]=644", "BAL: merchant=123456789", "BAL: merchant=111111"]

print(answer(input_3))

