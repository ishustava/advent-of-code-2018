records = []
with open("day4.txt") as f:
  records = f.readlines()

import re
DATE = '\[(\d+\-\d+\-\d+\s+\d+:\d+)\]\s+(.+)'
DAY = '\d+\-(\d+\-\d+)\s+\d+:\d+'
MINUTE = '\d+\-\d+\-\d+\s+\d+:(\d+)'
SLEEP = 'falls\s+asleep'
WAKE = 'wakes\s+up'
GUARD = 'Guard\s+#(\d+)\s+begins\s+shift'

records = [re.search(DATE, record).groups() for record in records]
records = {r[0]: r[1] for r in records}
times = list(records.keys())
times.sort()

guards = {}
gid = None
asleep = -1

for t in times:
  minute = int(re.search(MINUTE, t).group(1))
  g = re.search(GUARD, records[t])
  s = re.search(SLEEP, records[t])
  w = re.search(WAKE, records[t])
  if g:
    gid = int(g.group(1))
  if s:
    asleep = minute
  if w:
    if guards.get(gid, None) == None:
      guards[gid] = []
    day_mins = 60 * [0]
    for i in range(asleep, minute):
      day_mins[i] = 1
    guards[gid].append(day_mins)

total_guards = {gid: sum([n for m in mins for n in m]) for gid, mins in guards.items()}
max_guard = max(total_guards.keys(), key=(lambda k: total_guards[k]))
print(max_guard)
print(total_guards[max_guard])

max_min_i = -1
max_min = 0

for i in range(60):
  mins = sum([m[i] for m in guards[max_guard]])
  if mins > max_min:
    max_min = mins
    max_min_i = i

print(max_min_i * max_guard)

from functools import reduce
add_lists = lambda x, y: [a + b for a, b in zip(x, y)]
f_guards = {gid: list(reduce(add_lists, mins)) for gid, mins in guards.items()}
max_guards = {gid: max(mins) for gid, mins in f_guards.items()}
max_guard = max(max_guards.keys(), key=(lambda k: max_guards[k]))
print(max_guard)
most_asleep_min = f_guards[max_guard].index(max_guards[max_guard])
print(most_asleep_min)
print(most_asleep_min * max_guard)
