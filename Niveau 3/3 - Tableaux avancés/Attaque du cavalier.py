game = [['.' for _ in range(8)] for _ in range(8)]

for i in range(8):
    line = list(input())
    for pieceIndex in range(8):
        piece = line[pieceIndex]
        if piece.isalpha() and piece.islower():
            game[i][pieceIndex] = 'o'
        elif piece.isalpha() and piece == "C":
            game[i][pieceIndex] = 'C'

def check_knight(game):
    for i in range(8):
        for j in range(8):
            if game[i][j] == "C":
                couples = [
                    [i-2, j-1],
                    [i-1, j-2],
                    [i-2, j+1],
                    [i-1, j+2],
                    [i+2, j+1],
                    [i+1, j+2],
                    [i+2, j-1],
                    [i+1, j-2],
                ]
                for couple in couples:
                    try:
                        if game[couple[0]][couple[1]] == "o":
                            return True
                    except:
                        pass
    return False

if (check_knight(game)):
    print("yes")
else:
    print("no")