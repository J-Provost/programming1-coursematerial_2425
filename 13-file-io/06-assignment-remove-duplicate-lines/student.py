def remove_duplicate_lines(source, destination):
    with open(source, 'r') as infile, open(destination, 'w') as outfile:
        previous_line = None
        for line in infile:
            if line != previous_line:
                outfile.write(line)
                previous_line = line
