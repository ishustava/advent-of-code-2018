frequencies = []
with open("day1-input.txt") as f:
    frequencies = f.readlines()
frequencies = [int(f) for f in frequencies]


def find_first_repeating(frequencies):
  total = 0
  d = {total:0}
  repeated = None
  while repeated == None:
    for f in frequencies:
      total += f
      if d.get(total, None) != None:
        repeated = total
        break
      d[total] = 0 
  return repeated

print(find_first_repeating(frequencies))
print(find_first_repeating([1, -1]))
print(find_first_repeating([3, 3, 4, -2, -4]))
print(find_first_repeating([-6, 3, 8, 5, -6]))
print(find_first_repeating([7, 7, -2, -7, -4]))
