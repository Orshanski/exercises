def check_sq(my_sq):
    for i in range(3):
        for j in range(3):
            if my_sq[i][j] > 9:
                return False

    f_row = sum(my_sq[0])
    if not sum(my_sq[1]) == f_row:
        return False
    if not sum(my_sq[2]) == f_row:
        return False
    if not sum(list(zip(*my_sq))[0]) == f_row:
        return False
    if not sum(list(zip(*my_sq))[1]) == f_row:
        return False
    if not sum(list(zip(*my_sq))[2]) == f_row:
        return False
    if not (my_sq[0][0] + my_sq[1][1] + my_sq[2][2]) == f_row:
        return False
    if not (my_sq[0][2] + my_sq[1][1] + my_sq[2][0]) == f_row:
        return False
    return True


my_sq = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

if check_sq(my_sq):
    print('Yes')
else:
    print('No')