
__author__ = "Maximilian Geitner"
__date__ = "11.12.2023"

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    lines = []

    # lists containing index of empty rows or columns
    expanded_rows = []
    expanded_cols = []

    with open(filename) as file:

        for row_index, line in enumerate(file):
            line = line.replace("\n", "")
            # add expansion rows
            if len(line.replace(".", "")) == 0:
                expanded_rows.append(row_index)
                lines.append(line)
            else:
                lines.append(line)


    # 1.) Expand galaxies (columns)
    galaxies_pos = []
    for index in range(len(lines[0])):
        galaxy_count = 0
        for row_index in range(len(lines)):
            if lines[row_index][index] == '#':
                galaxy_count += 1
            if galaxy_count > 0:
                break
        if galaxy_count == 0:
            # expand galaxy
            expanded_cols.append(index)

    # 2.) Find galaxies
    cols = len(lines[0])
    rows = len(lines)
    for index in range(cols):
        for row_index in range(rows):
            if lines[row_index][index] == '#':
                galaxies_pos.append((index, row_index))

    # 3.) Calculate distances between galaxies
    total_dist = 0
    for i in range(len(galaxies_pos)):
        for j in range(i + 1, len(galaxies_pos)):
            source_galaxy_x, source_galaxy_y = galaxies_pos[i]
            target_galaxy_x, target_galaxy_y = galaxies_pos[j]
            dist = abs(source_galaxy_x - target_galaxy_x) + abs(source_galaxy_y - target_galaxy_y)
            expanded_galaxies_count = 0

            min_x = min(source_galaxy_x, target_galaxy_x)
            max_x = max(source_galaxy_x, target_galaxy_x)
            min_y = min(source_galaxy_y, target_galaxy_y)
            max_y = max(source_galaxy_y, target_galaxy_y)
            # look at expanded cols
            for x in range(min_x + 1, max_x):
                if x in expanded_cols:
                    expanded_galaxies_count += 1
            for y in range(min_y + 1, max_y):
                if y in expanded_rows:
                    expanded_galaxies_count += 1
            # 1000000
            dist += (1000000 - 1) * expanded_galaxies_count
            total_dist += dist

    print("Solution Day 11 Part 2: ", total_dist)
