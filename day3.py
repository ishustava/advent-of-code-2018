claims = []
with open("day3.txt") as f:
  claims = f.readlines()

import re
PATTERN = '#(\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)'
claims = [re.search(PATTERN, s).groups() for s in claims]
claims = [(int(c[0]), int(c[1]), int(c[2]), int(c[3]), int(c[4])) for c in claims]
points = {p[0]: [(p[1] + i, p[2] + j) for i in range(p[3]) for j in range(p[4])] for p in claims}
from collections import Counter
point_counts = Counter([p for id_points in points.values() for p in id_points ])
overlapping = list(filter(lambda x: x > 1, point_counts.values()))
print(len(overlapping))

overlapping = set([p for p in point_counts.keys() if point_counts[p] > 1])
for i, i_points in points.items():
  if not any([p for p in i_points if p in overlapping]):
    print(i)
    break
