def parse_input(input_string):
    return [list(line) for line in input_string.strip().split('\n')]

def find_locations(grid):
    locations = {}
    for row_idx, row in enumerate(grid):
        for col_idx, char in enumerate(row):
            if char != '.':
                if char not in locations:
                    locations[char] = []
                locations[char].append((row_idx, col_idx))
    return locations

def calculate_distances(locations):
    distances = {}
    for char, loc_list in locations.items():
        if len(loc_list) > 1:
            distances[char] = []
            for i in range(len(loc_list)):
                for j in range(i + 1, len(loc_list)):
                    location_a = loc_list[i]
                    location_b = loc_list[j]
                    down_steps = location_b[0] - location_a[0]
                    right_steps = location_b[1] - location_a[1]
                    distances[char].append((location_a, location_b, (down_steps, right_steps)))
    return distances


def add_hashes(grid, start_pos, steps, direction_multiplier):
    count_hashes = 0
    grid_size = (len(grid), len(grid[0]))
    next_pos = (start_pos[0] + direction_multiplier * steps[0],
                start_pos[1] + direction_multiplier * steps[1])

    next_pos = (next_pos[0] + direction_multiplier * steps[0],
                next_pos[1] + direction_multiplier * steps[1])

    while 0 <= next_pos[0] < grid_size[0] and 0 <= next_pos[1] < grid_size[1]:
        if grid[next_pos[0]][next_pos[1]] == '.':
            grid[next_pos[0]][next_pos[1]] = '#'
            count_hashes += 1
        else:
            count_hashes += 1
        next_pos = (next_pos[0] + direction_multiplier * steps[0],
                    next_pos[1] + direction_multiplier * steps[1])

    return count_hashes


def add_hash_between_duo(grid, loc_a, loc_b):
    # Calculate the differences in row and column
    dx = loc_b[0] - loc_a[0]
    dy = loc_b[1] - loc_a[1]

    # Check that both coordinates are divisible by 3 to be in line at 1:2
    if (dx % 3 == 0) and (dy % 3 == 0):
        # Calculate the 1:2 point
        point_1 = (loc_a[0] + dx // 3, loc_a[1] + dy // 3)

        # Ensure point_1 is within bounds and on a line with loc_a and loc_b
        if 0 <= point_1[0] < len(grid) and 0 <= point_1[1] < len(grid[0]):
            grid[point_1[0]][point_1[1]] = '#'


def overlay_hashes_on_grid(grid, distances):
    display_grid = [row[:] for row in grid]
    total_possible_hashes = 0

    for char, distance_list in distances.items():
        print(f"Character {char}:")
        for (loc_a, loc_b, (down, right)) in distance_list:
            # Add # between the duo in a straight line (vertically, horizontally, diagonally)
            add_hash_between_duo(display_grid, loc_a, loc_b)

            # Add '#' outside the character duo
            duo_hash_count = (add_hashes(display_grid, loc_a, (down, right), 1) +
                              add_hashes(display_grid, loc_b, (down, right), -1))
            total_possible_hashes += duo_hash_count
            print(f"  Pair {loc_a} to {loc_b} can add {duo_hash_count} '#'")

    return display_grid, total_possible_hashes


def is_line_clear(grid, start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]

    steps = max(abs(dx), abs(dy))
    x_step = dx / steps
    y_step = dy / steps

    for k in range(1, steps):
        nx = int(round(start[0] + k * x_step))
        ny = int(round(start[1] + k * y_step))
        if grid[nx][ny] != '.':
            return False

    return True

def find_intact_duos(grid, distances):
    intact_duos = []

    for char, distance_list in distances.items():
        for (loc_a, loc_b, _) in distance_list:
            if is_line_clear(grid, loc_a, loc_b):
                intact_duos.append((loc_a, loc_b))

    return intact_duos

def count_characters(locations):
    return {char: len(locs) for char, locs in locations.items()}

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def count_positions_in_multiple_duos(duos):
    position_count = {}

    for loc_a, loc_b in duos:
        for loc in [loc_a, loc_b]:
            if loc not in position_count:
                position_count[loc] = 0
            position_count[loc] += 1

    count_more_than_one = 0
    print("\nPositions appearing in more than one duo:")
    for loc, count in position_count.items():
        if count > 1:
            print(f"  Position {loc} appears in {count} duos.")
            count_more_than_one += 1

    return count_more_than_one, [loc for loc, count in position_count.items() if count > 1]


def main(input_string):
    grid = parse_input(input_string)
    character_locations = find_locations(grid)

    character_counts = count_characters(character_locations)
    for char, count in character_counts.items():
        print(f"Character '{char}' appears {count} times.")

    character_distances = calculate_distances(character_locations)

    display_grid, total_possible_hashes = overlay_hashes_on_grid(grid, character_distances)

    intact_duos = find_intact_duos(display_grid, character_distances)
    print("\nList of intact duos with conditions met:")
    for duo in intact_duos:
        print(f"  Duo from {duo[0]} to {duo[1]} remains intact.")

    print(f"Total number of '#' that can be placed: {total_possible_hashes}")

    positions_more_than_one_duo, _ = count_positions_in_multiple_duos(intact_duos)

    sum_total = total_possible_hashes + positions_more_than_one_duo
    print(f"\nSum of total '#' placed and positions appearing in more than one duo: {sum_total}")

    print("\nFinal modified grid:")
    print_grid(display_grid)

input_string = """
...s..............................................
...................w......K.......t...............
........s.........................................
.......s......w...............1...................
.........w5.......................................
.......................t.F........................
..................................................
F................................1...........d....
.........................5......................K.
............5.................R..............KZ...
....F.....q.........w..............1.....t........
............8.......I.............................
..........8.................t....................K
...........8.................5.....Z..............
.........q..............................Z...d..U..
...................Y.q...R........................
....................E.....z...............y.......
..........................................U.......
.....F.................................k........S.
............q...................d.................
.................................R................
..x....................................U.........y
.......x.........................E..M...U..d......
......z.......X............................4......
...............I....m....M......R............y....
.......z...................................k..e...
..f..z.......................................e....
...f.I..........7..u..........M................D..
.......X..I.......x.................k.............
.........X.......7....................4.......S...
....................u9...T.....3.Z....o..........6
........f.......D..3....u..................S......
...W...0.........................................D
.....................T................E.......m...
...8....Y............f........T4..................
......Y...........................................
....0.............3...............................
....................3.T.....................k.....
.......................u..............6...........
...........................6..........9........e..
..................4....7.............o..........D.
.................................M...E..o.........
...i.................O...........................Q
.....0.i.....................................m.2..
.......Y.r........7..............S..O..2.......m..
.....r......0.............O.......................
..................................Q...............
........................6................o......Q.
..W...r.................................9.........
.W.........................O........2.............
"""

main(input_string)