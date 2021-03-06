# Standard library imports
import os
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OBSTACLE = "+"
PATH = " "
START = "S"


# Generates random maze of size nxm
def generate_maze(rows, columns, file_name):
    # Appends text extension if not specified\
    if not ".txt" in file_name:
        file_name += ".txt"

    # Opens file if it exists, if not, create one
    new_file = os.path.join(BASE_DIR, file_name)
    maze_file = open(new_file, "w+")

    # Generates start row and column for the maze
    start = generate_random_start(rows, columns)

    # Populates maze_file
    maze_file.write(OBSTACLE * columns + "\n")
    for row in range(0, rows - 2):
        for column in range(0, columns):
            if row == start[0] and column == start[1]:
                maze_file.write("S")
            else:
                maze_file.write(random.choice([OBSTACLE, PATH]))
        maze_file.write("\n")
    maze_file.write(OBSTACLE * columns + "\n")

    # Closes file when finished
    maze_file.close()


def generate_random_start(rows, columns):
    start_row = random.randrange(1, rows)
    start_column = random.randrange(1, columns)
    return [start_row, start_column]


def read_maze(file_name):
    # Appends text extension if not specified
    if not ".txt" in file_name:
        file_name += ".txt"

    # Opens file if it exists
    new_file = os.path.join(BASE_DIR, file_name)
    maze_file = open(new_file, "r")
    if maze_file.mode == "r":
        content = maze_file.read()
        print(content)

    # Closes file when finished
    maze_file.close()


def main():
    generate_maze(11, 22, "maze_test")
    read_maze("maze_test")


if __name__ == "__main__":
    main()
