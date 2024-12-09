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


def add_outward_hashes(grid, start_pos, steps, direction_multiplier):
    grid_size = (len(grid), len(grid[0]))
    positions = set()
    current_pos = (start_pos[0] + direction_multiplier * steps[0],
                   start_pos[1] + direction_multiplier * steps[1])

    while 0 <= current_pos[0] < grid_size[0] and 0 <= current_pos[1] < grid_size[1]:
        positions.add(current_pos)
        current_pos = (current_pos[0] + direction_multiplier * steps[0],
                       current_pos[1] + direction_multiplier * steps[1])

    for pos in positions:
        grid[pos[0]][pos[1]] = '#'

    return positions


def overlay_hashes_on_grid(grid, distances):
    display_grid = [row[:] for row in grid]
    all_hash_positions = set()

    for char, distance_list in distances.items():
        print(f"Character {char}:")
        for (loc_a, loc_b, (down, right)) in distance_list:
            # Add '#' extending outward from both ends of the line formed by loc_a and loc_b
            positions_a_extend = add_outward_hashes(display_grid, loc_a, (down, right), -1)
            all_hash_positions.update(positions_a_extend)

            positions_b_extend = add_outward_hashes(display_grid, loc_b, (down, right), 1)
            all_hash_positions.update(positions_b_extend)

            print(f"  Extending from {loc_a} and {loc_b} outward processed for '#' addition.")

    return display_grid


def convert_repeated_characters_to_hashes(grid, character_counts):
    for row_idx, row in enumerate(grid):
        for col_idx, char in enumerate(row):
            if char in character_counts and character_counts[char] > 1:
                grid[row_idx][col_idx] = '#'


def count_characters(locations):
    return {char: len(locs) for char, locs in locations.items()}


def count_hashes_in_grid(grid):
    return sum(row.count('#') for row in grid)


def print_grid(grid):
    for row in grid:
        print(''.join(row))


def main(input_string):
    grid = parse_input(input_string)
    character_locations = find_locations(grid)
    character_counts = count_characters(character_locations)

    for char, count in character_counts.items():
        print(f"Character '{char}' appears {count} times.")

    character_distances = calculate_distances(character_locations)

    display_grid = overlay_hashes_on_grid(grid, character_distances)

    convert_repeated_characters_to_hashes(display_grid, character_counts)

    total_hashes = count_hashes_in_grid(display_grid)

    print(f"Total '#' in final grid: {total_hashes}")
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