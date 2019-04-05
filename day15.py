from queue import Queue


# turn:
# identify all targets; if no targets, combat ends
# identify all open squares in range of all targets
# to move, consider all squares that are in range
# choose square that can be reached in fewest number of steps
# takes steps along the shortest path to the chosen square


def is_adjacent(loc1, loc2):
    x1, y1 = loc1
    x2, y2 = loc2

    if abs(x1 - x2) == 1 and y1 == y2:
        return True

    if abs(y1 - y2) == 1 and x1 == x2:
        return True

    return False


def adjacent_locations(grid, location):
    x, y = location
    manhattan_adjacent = [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]
    return [p for p in manhattan_adjacent if grid.get(p) and grid[p] == '.']


def greater_in_reading_order(l1, l2):
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            if l1[i][1] < l2[i][1]:
                return True
            else:
                return False


class Unit:
    def __init__(self, current_location, attack_power=3):
        self.current_location = current_location
        self.attack_power = attack_power
        self.hit_points = 200
        self.current_path = None
        self.target_square = None

    def play_turn(self, enemy_units, grid):
        if self.hit_points <= 0:
            return None, grid

        enemy_in_range = self.find_enemy_in_range(enemy_units)

        if not enemy_in_range:
            grid = self.move(grid, enemy_units)
            enemy_in_range = self.find_enemy_in_range(enemy_units)

        if enemy_in_range:
            self.attack(enemy_in_range)
            return enemy_in_range, grid

        return None, grid

    def move(self, grid, enemy_units):
        # define all open squares in range of all enemy units
        # find shortest path to each of those squares
        # find the shortest of those in reading order
        # save it as current target and current path
        enemy_squares_in_range = [l for enemy_unit in enemy_units for l in
                                  adjacent_locations(grid, enemy_unit.current_location)]

        enemy_shortest_path = self.shortest_path(grid, enemy_squares_in_range)

        if enemy_shortest_path:
            next_location = enemy_shortest_path[0]
            grid[self.current_location], grid[next_location] = '.', grid[self.current_location]
            self.current_location = next_location

        return grid

    def find_enemy_in_range(self, enemy_units):
        enemies_in_range = list(filter(lambda x: is_adjacent(self.current_location, x.current_location), enemy_units))
        return min(enemies_in_range, key=lambda x: x.hit_points) if enemies_in_range else enemies_in_range

    def shortest_path(self, grid, destinations):
        min_distance = float('inf')
        min_destination = None

        visited = set()
        added = set()

        desired_visited = set(destinations)

        paths = {self.current_location: []}

        pq = Queue()
        pq.put_nowait((len(paths[self.current_location]), self.current_location))
        while not pq.empty() and desired_visited:
            current_distance, current = pq.get_nowait()

            for n in adjacent_locations(grid, current):
                if n not in visited:
                    if not paths.get(n):
                        paths[n] = paths[current] + [n]
                    else:
                        new_path = paths[current] + [n]
                        if len(paths[n]) > current_distance + 1:
                            paths[n] = new_path
                    if n not in added:
                        pq.put_nowait((len(paths[n]), n))
                        added.add(n)

            visited.add(current)

            if current in desired_visited:
                desired_visited.remove(current)
                if len(paths[current]) < min_distance:
                    min_distance = len(paths[current])
                    min_destination = current
            remaining = [len(paths[d]) for d in desired_visited if paths.get(d)]
            if remaining and min(remaining) > min_distance:
                break

        return paths.get(min_destination)

    def attack(self, enemy):
        enemy.hit_points -= self.attack_power

    def __str__(self):
        return str(self.current_location) + ";" + str(self.hit_points)

    def __repr__(self):
        s = ''
        if type(self) == Elf:
            s += 'E:'
        else:
            s += 'G:'
        return s + "(" + str(self.current_location) + ", " + str(self.hit_points) + ")"


class Elf(Unit):
    pass


class Goblin(Unit):
    pass


class Combat:
    def __init__(self, grid, elf_attack_power=3):
        self.grid = grid
        self.units = []
        self.elf_died = False

        for location, item in grid.items():
            if item == 'G':
                self.units.append(Goblin(location))
            elif item == 'E':
                self.units.append(Elf(location, elf_attack_power))

        self.units = sorted(self.units, key=lambda x: (x.current_location[1], x.current_location[0]))

    def play_one_round(self):
        to_remove = set()
        for unit in self.units:
            enemy_units = self.enemy_units_to(unit)
            attacked, self.grid = unit.play_turn(enemy_units, self.grid)

            if attacked and attacked.hit_points <= 0:
                if type(attacked) == Elf:
                    self.elf_died = True

                to_remove.add(attacked)
                self.grid[attacked.current_location] = '.'

        self.units = [u for u in self.units if u not in to_remove]
        self.units = sorted(self.units, key=lambda x: (x.current_location[1], x.current_location[0]))

    def enemy_units_to(self, unit):
        return [u for u in self.units if type(u) != type(unit) and u.hit_points > 0]

    def elfs(self):
        return [unit for unit in self.units if type(unit) == Elf and unit.hit_points > 0]

    def goblins(self):
        return [unit for unit in self.units if type(unit) == Goblin and unit.hit_points > 0]

    def ended(self):
        if len(self.elfs()) == 0 or len(self.goblins()) == 0:
            return True

        return False

    def winner_points(self):
        if len(self.elfs()) == 0:
            return sum([x.hit_points for x in self.goblins()])
        else:
            return sum([x.hit_points for x in self.elfs()])


def load_input(file):
    rows = []
    with open(file) as f:
        rows = f.readlines()
    grid_h = len(rows)
    grid_w = len(rows[0].strip())
    gr = {}
    for i in range(len(rows)):
        for j in range(len(rows[i].strip())):
            gr[(j, i)] = rows[i][j]
    return gr, grid_h, grid_w


def print_grid(g, h, w):
    for i in range(h):
        row = ''
        for j in range(w):
            row += g[(j, i)]

        print(row)


grid, grid_h, grid_w = load_input("test.txt")
round = 0

# PART I
combat = Combat(grid, 15)
while not combat.ended():
    round += 1
    combat.play_one_round()
    print("round:", round)
    print_grid(combat.grid, grid_h, grid_w)
    print(combat.units)

print(combat.winner_points(), round - 1)

# PART II
# attack_power = 4
# combat = Combat(grid, attack_power)
#
# while True:
#     grid, grid_h, grid_w = load_input("test.txt")
#     combat = Combat(grid, attack_power)
#     round = 0
#     print("attack power:", attack_power)
#     print_grid(grid, grid_h, grid_w)
#     while not combat.ended() and not combat.elf_died:
#         round += 1
#         combat.play_one_round()
#         # print("round:", round)
#
#     if not combat.elf_died:
#         break
#
#     attack_power += 1
#
# print()
# print_grid(combat.grid, grid_h, grid_w)
# print(combat.units)
# print(combat.winner_points(), (round))
