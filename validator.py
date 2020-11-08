def valide_line_and_no_zero(board):
    errors = 0
    for i in board:
        if i.count(0) != 0:
            errors += 1
        for j in i:
            if i.count(j) > 1:
                errors += 1
    return errors == 0


def valide_column(board):
    colonnes = []
    for i in range(len(board)):
        colonne = []
        for j in board:
            colonne += [j[i]]
        colonnes += [colonne]
        
    return valide_line_and_no_zero(colonnes)


def valid_square(board):
    errors = 0
    all_square = []
    d = [3, 6, 9]
    t = []
    for i in d:
        for line in board:
            t += [line[(i - 3):i]]
            if len(t) == 3:
                all_square += [t]
                t = []

    for i in all_square:
        square = []
        for j in i:
            square += j
        for i in square:
            if square.count(i) > 1:
                errors += 1
    return errors == 0

def valid_solution(board):
    return valide_line_and_no_zero(board) == valide_column(board)\
== valid_square(board) == True