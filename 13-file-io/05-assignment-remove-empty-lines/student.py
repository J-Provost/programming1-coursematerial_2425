def remove_empty_lines(source, destination):
    with open(source, 'r') as infile:
        lines = [line for line in infile if line.strip() or line != "\n"] 

    with open(destination, 'w') as outfile:
        outfile.writelines(lines)