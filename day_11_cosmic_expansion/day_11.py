
__author__ = "Maximilian Geitner"
__date__ = "11.12.2023"

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    lines = []
    galaxy = []
    # 1.) Initialize Setup
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            # add expansion rows
            if len(line.replace(".", "")) == 0:
                lines.append(line)
                lines.append(line)
                galaxy.append([])
                galaxy.append([])
            else:
                lines.append(line)
                galaxy.append([])

    # 2.) Expand galaxies (columns)
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
            for row_index in range(len(lines)):

                galaxy[row_index].append('.')
                galaxy[row_index].append('.')
        else:
            for row_index in range(len(lines)):
                galaxy[row_index].append(lines[row_index][index])

    # 3.) Find galaxies
    cols = len(galaxy[0])
    rows = len(galaxy)
    for index in range(cols):
        for row_index in range(rows):
            if galaxy[row_index][index] == '#':
                galaxies_pos.append((index, row_index))

    # 4.) Calculate distances between galaxies
    total_dist = 0
    for i in range(len(galaxies_pos)):
        for j in range(i + 1, len(galaxies_pos)):
            source_galaxy_x, source_galaxy_y = galaxies_pos[i]
            target_galaxy_x, target_galaxy_y = galaxies_pos[j]
            dist = abs(source_galaxy_x - target_galaxy_x) + abs(source_galaxy_y - target_galaxy_y)
            total_dist += dist
    print("Solution Day 11 Part 1: ", total_dist)
