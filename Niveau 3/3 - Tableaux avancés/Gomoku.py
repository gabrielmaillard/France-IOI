def generate_game(size):
    game = [['' for _ in range(size)] for _ in range(size)]
    for i in range(size):
        line = input().split(" ")
        for j in range(size):
            game[i][j] = line[j]
    return game

def check_win(game, player):
    target = str(player) * 5
    for line in game:
        if target in ''.join(line):
            return True
    for i in range(len(game)):
        column_concat = ''.join([line[i] for line in game])
        if target in column_concat:
            return True
    for i in range(len(game)):
        for j in range(len(game)):
            if i + 4 < len(game) and j + 4 < len(game):
                diag1 = ''.join([game[i+k][j+k] for k in range(5)])
                diag2 = ''.join([game[i+k][j+4-k] for k in range(5)])
                if target in diag1 or target in diag2:
                    return True
    return False

game = generate_game(int(input()))
if check_win(game, 1):
    print(1)
elif check_win(game, 2):
    print(2)
else:
    print(0)
