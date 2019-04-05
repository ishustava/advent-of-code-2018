p = ""
with open("day5.txt") as f:
  p = f.read()

units = set(p.lower())

def react(p):
  while True:
    can_be_destroyed = False
    original = p
    for u in units:
      p = p.replace(u+u.upper(), "")
      p = p.replace(u.upper()+u, "")
    if len(p) == len(original):
      break
  return p

print(len(react(p)))

min_len = len(p)

for u in units:
  test = p.replace(u, "")
  test = test.replace(u.upper(), "")
  reacted = react(test)
  if len(reacted) < min_len:
    min_len = len(reacted)

print(min_len)
