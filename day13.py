track_rows = []

with open("day13.txt") as f:
    track_rows = f.readlines()

grid = {}
carts = []
cart_orientation_to_track_orientation = {'<': '-', '^': '|', 'v': '|', '>': '-'}

for i in range(len(track_rows)):
    for j in range(len(track_rows[i])):
        track_char = track_rows[i][j]
        if track_char != ' ' and track_char != '\n':
            grid[(j, i)] = track_char
        if track_char in ['<', '>', '^', 'v']:
            carts.append((j, i, 0, track_char))
            grid[(j, i)] = cart_orientation_to_track_orientation[track_char]


def move_cart_in_direction(cart_info, track_orientation):
    x, y, num_intersections, cart_orientation = cart_info
    if track_orientation == '|':
        if cart_orientation == '^':
            return x, y - 1, num_intersections, '^'
        elif cart_orientation == 'v':
            return x, y + 1, num_intersections, 'v'

    elif track_orientation == '-':
        if cart_orientation == '>':
            return x + 1, y, num_intersections, '>'
        elif cart_orientation == '<':
            return x - 1, y, num_intersections, '<'

    elif track_orientation == '/':
        if cart_orientation == '^':
            return x + 1, y, num_intersections, '>'
        if cart_orientation == 'v':
            return x - 1, y, num_intersections, '<'
        if cart_orientation == '>':
            return x, y - 1, num_intersections, '^'
        if cart_orientation == '<':
            return x, y + 1, num_intersections, 'v'

    elif track_orientation == '\\':
        if cart_orientation == '^':
            return x - 1, y, num_intersections, '<'
        if cart_orientation == 'v':
            return x + 1, y, num_intersections, '>'
        if cart_orientation == '>':
            return x, y + 1, num_intersections, 'v'
        if cart_orientation == '<':
            return x, y - 1, num_intersections, '^'

    elif track_orientation == '+':
        if cart_orientation == '>':
            if num_intersections % 3 == 0:
                return x, y - 1, num_intersections + 1, '^'
            if num_intersections % 3 == 1:
                return x + 1, y, num_intersections + 1, '>'
            if num_intersections % 3 == 2:
                return x, y + 1, num_intersections + 1, 'v'

        elif cart_orientation == '<':
            if num_intersections % 3 == 0:
                return x, y + 1, num_intersections + 1, 'v'
            if num_intersections % 3 == 1:
                return x - 1, y, num_intersections + 1, '<'
            if num_intersections % 3 == 2:
                return x, y - 1, num_intersections + 1, '^'

        elif cart_orientation == 'v':
            if num_intersections % 3 == 0:
                return x + 1, y, num_intersections + 1, '>'
            if num_intersections % 3 == 1:
                return x, y + 1, num_intersections + 1, 'v'
            if num_intersections % 3 == 2:
                return x - 1, y, num_intersections + 1, '<'

        elif cart_orientation == '^':
            if num_intersections % 3 == 0:
                return x - 1, y, num_intersections + 1, '<'
            if num_intersections % 3 == 1:
                return x, y - 1, num_intersections + 1, '^'
            if num_intersections % 3 == 2:
                return x + 1, y, num_intersections + 1, '>'


# found_collision = False
# while not found_collision:
#
#     for i in range(len(carts)):
#         cart = carts[i]
#         current_location = cart[:2]
#         carts[i] = move_cart_in_direction(cart, grid[current_location])
#
#         next_location = carts[i][:2]
#         carts_locations = set([(c[0], c[1]) for c in carts if c != carts[i]])
#         if next_location in carts_locations:
#             found_collision = True
#             print("collision: ", next_location)
#             break
#
#     carts = sorted(carts, key=lambda x: (x[1], x[0]))
carts = sorted(carts, key=lambda x: (x[1], x[0]))
while len(carts) - carts.count(None) != 1:
    print(carts)
    for i in range(len(carts)):
        cart = carts[i]
        if cart:
            current_location = cart[:2]
            carts[i] = move_cart_in_direction(cart, grid[current_location])

            next_location = carts[i][:2]
            carts_locations = set([(c[0], c[1]) for c in carts if c != carts[i] and c])
            if next_location in carts_locations:
                carts[i] = None
                other_car_i = [j for j in range(len(carts)) if carts[j] and carts[j][:2] == next_location][0]
                carts[other_car_i] = None

                print("collision: ", next_location)

    carts = sorted([c for c in carts if c], key=lambda x: (x[1], x[0]))

print([c for c in carts if c])