input_text = "476 players; last marble is worth 71657 points"
# input_text = "17 players; last marble is worth 1104 points"
# input_text = "9 players; last marble is worth 25 points"
REGEX = '(\d+) players; last marble is worth (\d+) points'

num_players = 476
num_marbles = 71657

# scores = {i: 0 for i in range(num_players)}
# circle = [0]
# current_marble_i = 0
#
# for marble in range(1, num_marbles + 1):
#     player = marble % num_players
#
#     if marble % 100000 == 0:
#         print(marble)
#     if marble % 23 == 0:
#         scores[player] += marble
#         to_remove = circle[current_marble_i - 7]
#         scores[player] += to_remove
#         current_marble_i = (current_marble_i - 7) % len(circle)
#         circle.pop(current_marble_i)
#         continue
#
#     current_marble_i = (current_marble_i + 1) % len(circle) + 1
#     circle.insert(current_marble_i, marble)
#
# print(scores)
# print(max(scores.values()))


class Node:
    def __init__(self, number):
        self.number = number
        self.clockwise = self
        self.counterclockwise = self

    def __init__(self, number, clockwise=None, counterclockwise=None):
        self.number = number
        self.clockwise = clockwise
        self.counterclockwise = counterclockwise

    def __str__(self):
        return str(self.number)


class Circle:
    def __init__(self, current_marble):
        self.current_marble = current_marble

    def add_one_clockwise(self, item):
        # find position that is one over
        # in the clockwise direction
        one_cw_marble = self.current_marble.clockwise
        two_cw_marble = self.current_marble.clockwise.clockwise
        new_marble = Node(item, two_cw_marble, one_cw_marble)
        one_cw_marble.clockwise = new_marble
        two_cw_marble.counterclockwise = new_marble
        self.current_marble = new_marble
        return new_marble

    def remove_7_counterclockwise(self):
        current = self.current_marble
        for i in range(7):
            current = current.counterclockwise
        cw = current.clockwise
        ccw = current.counterclockwise
        ccw.clockwise = cw
        cw.counterclockwise = ccw
        self.current_marble = cw
        return current


scores = {i: 0 for i in range(num_players)}
first = Node(0)
first.clockwise = first
first.counterclockwise = first
circle = Circle(first)

for marble in range(1, num_marbles + 1):
    player = marble % num_players

    # if marble % 1000000 == 0:
    #     print(marble)
    if marble % 23 == 0:
        scores[player] += marble
        removed = circle.remove_7_counterclockwise()
        scores[player] += removed.number
        continue

    circle.add_one_clockwise(marble)

# print(scores)
print(max(scores.values()))