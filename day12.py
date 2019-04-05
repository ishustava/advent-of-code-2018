import re

initial_state = "#..####.##..#.##.#..#.....##..#.###.#..###....##.##.#.#....#.##.####.#..##.###.#.......#............"
# initial_state = "#..#.#..##......###...###"

note_lines = []
with open("day12.txt") as f:
    note_lines = f.readlines()

NOTE_REGEX = '([\.#]+)\s+=>\s+([\.#])'
notes = {}
for n in note_lines:
    pots_config, prediction = re.search(NOTE_REGEX, n).groups()
    notes[pots_config] = prediction

num_generations = 132
redundant_dots = num_generations

current_state = initial_state
current_state = redundant_dots * '.' + current_state + redundant_dots * '.'
current_state = [c for c in current_state]
offset = 0

def last_index_of(l, c):
    last_i = 0
    for i in range(len(l)):
        if l[i] == c:
            last_i = i
    return last_i


def add_redundant_empty_pots(state):
    first_i = state.index('#')
    state = ['.'] * (redundant_dots - first_i) + state

    # last_i = last_index_of(state, '#')
    state = state + ['.'] * redundant_dots

    return state


for gen in range(num_generations):
    # next_state = add_redundant_empty_pots(current_state)
    next_state = current_state[:]

    print(gen, ''.join(current_state))

    for i in range(len(current_state) - 5):
        pot_cfg = ''.join(current_state[i:i + 5])
        if notes.get(pot_cfg):
            next_state[i + 2] = notes[pot_cfg]
        else:
            next_state[i + 2] = '.'

    current_state = next_state

print(num_generations, ''.join(current_state)[num_generations:])
print(sum([i - redundant_dots for i in range(len(current_state)) if current_state[i] == '#']))