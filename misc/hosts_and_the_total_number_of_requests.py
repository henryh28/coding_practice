# read the string filename
filename = input()
count = {}
keys = []

file = open(filename, "r")

output = open("records_hosts_access_log_00.txt", "a")

data = file.readlines()
file.close()

for string in data:
  host = string.split()[0]
  count[host] = 1 if host not in count else count[host] + 1
  if host not in keys:
    keys.append(host)

keys.sort()

for key in keys:
  line = key + " " + str(count[key])
  output.write(line)

print(output)
