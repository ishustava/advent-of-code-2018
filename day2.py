ids = []
with open("day2.txt") as f:
    ids = f.readlines()

from collections import Counter
c_ids = [Counter(i) for i in ids]
num2s = 0
num3s = 0

for c_id in c_ids:
  nums = set(c_id.values())
  for n in nums:
    if n == 2:
      num2s += 1
    elif n == 3:
      num3s += 1
        
   
print(num2s, num3s, num2s * num3s)

def differ_by_one(s1, s2):
  diff_ind = -1
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      if diff_ind != -1:
        return -1
      diff_ind = i
  return diff_ind

found = False
while not found:
  id = ids.pop()
  for i in ids:
    didx = differ_by_one(id, i)
    if didx != -1:
      found = True
      print(id, i, id[:didx] + id[didx + 1:])
      break
