import re

point_lines = []
with open("day10.txt") as f:
    point_lines = f.readlines()

POINT_VELOCITY_REGEX = 'position=<\s*([-]*\d+),\s+([-]*\d+)>\s+velocity=<\s*([-]*\d+),\s+([-]*\d+)>'

points = []
velocities = []
for p in point_lines:
    x, y, v_x, v_y = re.search(POINT_VELOCITY_REGEX, p).groups()
    points.append((int(x), int(y)))
    velocities.append((int(v_x), int(v_y)))

x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]
min_x, max_x = min(x_coords), max(x_coords)
min_y, max_y = min(y_coords), max(y_coords)

print(points)


def print_points(pts, min_x, max_x, min_y, max_y):
    for y in range(min_y, max_y + 1):
        line = ''
        for x in range(min_x, max_x + 1):
            if (x, y) in pts:
                line += '#'
            else:
                line += '.'
        print(line)


def move_points(pts):
    return [(pts[i][0] + velocities[i][0], pts[i][1] + velocities[i][1]) for i in range(len(pts))]

seconds = 0
while True:
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    if abs(max_x) - abs(min_x) < 100:
        print("x range: ", str(min_x) + "-" + str(max_x))
        print("y range: ", str(min_y) + "-" + str(max_y))
        print("seconds: ", seconds)
        print_points(points, min_x, max_x, min_y, max_y)
    points = move_points(points)
    seconds += 1
