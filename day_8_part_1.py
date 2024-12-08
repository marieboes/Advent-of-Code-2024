def parse_input(input_string):
    return [list(line) for line in input_string.strip().split('\n')]

def find_locations(grid):
    # Dictionary to store found locations for each character
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
        if len(loc_list) > 1:  # We only care about characters that appear more than once
            distances[char] = []
            for i in range(len(loc_list)):
                for j in range(i + 1, len(loc_list)):
                    location_a = loc_list[i]
                    location_b = loc_list[j]
                    # Calculate distance in terms of steps down and steps right
                    down_steps = location_b[0] - location_a[0]
                    right_steps = location_b[1] - location_a[1]
                    distances[char].append((location_a, location_b, (down_steps, right_steps)))

    return distances

def modify_grid_with_hashes(grid, distances):
    for distance_list in distances.values():
        for (loc_a, loc_b, (down, right)) in distance_list:
            # Calculate negative and positive positions
            negative_pos = (loc_a[0] - down, loc_a[1] - right)
            positive_pos = (loc_b[0] + down, loc_b[1] + right)

            # Mark '#' on negative step position if within grid
            if 0 <= negative_pos[0] < len(grid) and 0 <= negative_pos[1] < len(grid[0]):
                grid[negative_pos[0]][negative_pos[1]] = '#'

            # Mark '#' on positive step position if within grid
            if 0 <= positive_pos[0] < len(grid) and 0 <= positive_pos[1] < len(grid[0]):
                grid[positive_pos[0]][positive_pos[1]] = '#'

    # Count unique '#' hashes from the modified grid
    num_hashes_added = sum(row.count('#') for row in grid)
    return num_hashes_added, grid

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def main(input_string):
    grid = parse_input(input_string)
    character_locations = find_locations(grid)
    character_distances = calculate_distances(character_locations)

    # Modify grid and count hashes added
    num_hashes_added, modified_grid = modify_grid_with_hashes(grid, character_distances)

    # Print the modified grid
    print("Modified Grid:")
    print_grid(modified_grid)

    # Output number of unique '#' characters added
    print(f"Number of unique '#' placements: {num_hashes_added}")
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