num_columns, num_lines = map(int, input().split())

# Matrice du labyrinthe
labyrinth = [list(input()) for _ in range(num_lines)]

# LES COORDONNEES SONT TOUJOURS SOUS LA FORME Y ; X
starting_position = (1, 0)

# Les déplacements sont triés dans l'ordre de priorité E, N, O, S
movements = [
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 0),
]

letters = ["E", "N", "O", "S"]

# Utilisation de la récursivité
def test_for_N_movements(num_movements, starting_position, labyrinth, sequence):
    if num_movements <= 0:
        return 
    if starting_position == (num_lines - 1, num_columns - 2): # Arrivee à la fin du labyrinthe
        print(len(sequence))
        print(sequence)
        exit()

    labyrinth[starting_position[0]][starting_position[1]] = "#"

    for index_neighbour, neighbour in enumerate(movements):
        new_y = neighbour[0] + starting_position[0]
        new_x = neighbour[1] + starting_position[1]
        if 0 <= new_y < num_lines and 0 <= new_x < num_columns and labyrinth[new_y][new_x] == ".":
            test_for_N_movements(num_movements - 1, (new_y, new_x), labyrinth, sequence+letters[index_neighbour])

    labyrinth[starting_position[0]][starting_position[1]] = "."

arrival = False
max_movements = 1
while not arrival:
    test_for_N_movements(max_movements, starting_position, labyrinth, "")
    max_movements += 1