manhattan_distance = lambda x, y: abs(x[0]-y[0]) + abs(x[1]-y[1])

points = []
with open("day6.txt") as f:
  points = f.readlines()

points = [p.split(",") for p in points]
points = [(int(p[0]), int(p[1])) for p in points]
x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]
min_x, max_x = min(x_coords), max(x_coords)
min_y, max_y = min(y_coords), max(y_coords)

distances = {p:0 for p in points}

def closest_point(points, p):
  dists = [manhattan_distance(p, point) for point in points]
  min_dist = min(dists)
  min_dists = [d for d in dists if d == min_dist]
  if len(min_dists) == 1:
    return points[dists.index(min_dist)]

non_inf = set(points)
for x in range(min_x - 1, max_x + 1):
  for y in range(min_y - 1, max_y + 1):
    cp = closest_point(points, (x, y))
    if cp != None:
      distances[cp] += 1
      on_boundary = x == min_x - 1 or x == max_x or y == min_y - 1 or y == max_y
      if on_boundary and cp in non_inf:
        non_inf.remove(cp)

non_inf_dist = {p:d for p, d in distances.items() if p in non_inf}
max_dist = max(non_inf_dist.values())

print(max_dist)

all_dist = {(x,y): sum([manhattan_distance(p, (x,y)) for p in points]) for x in range(min_x - 1, max_x + 1) for y in range(min_y - 1, max_y + 1)}
closest_region = {p: dist for p, dist in all_dist.items() if dist < 10000}
print(len(closest_region))
