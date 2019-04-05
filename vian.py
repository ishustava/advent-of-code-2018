a = "37"
p1 = 0
p2 = 1

while "077201" not in a[len(a) - 10:]:
  if len(a) % 100000 == 0:
    print(len(a), p1, p2)
  a_p1 = int(a[p1])
  a_p2 = int(a[p2])
  next_a = a_p1 + a_p2
  a += str(next_a)
  p1 = (p1 + a_p1 + 1) % len(a)
  p2 = (p2 + a_p2 + 1) % len(a)
print(a[5:15])
print(a[18:28])
print(a[2018:2028])
print(a[330121:330131])
print(a.index("077201"))
