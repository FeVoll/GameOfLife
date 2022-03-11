def near00(list, n, m, neig):
    count = 0
    for row in range(2):
        for col in range(2):
            if row + col != 0:
                if str(list[n + row][m + col]) == neig:
                    count += 1
    return count


def near01(list, n, m, neig):
    count = 0
    for row in range(2):
        for col in range(2):
            if row + col != 0:
                if str(list[n + row][m - col]) == neig:
                    count += 1
    return count


def near10(list, n, m, neig):
    count = 0
    for row in range(2):
        for col in range(2):
            if row + col != 0:
                if str(list[n - row][m + col]) == neig:
                    count += 1
    return count


def near11(list, n, m, neig):
    count = 0
    for row in range(2):
        for col in range(2):
            if row + col != 0:
                if str(list[n - row][m - col]) == neig:
                    count += 1
    return count


def nearup(list, n, m, neig):
    count = 0
    for row in range(2):
        for col in range(2):
            if row + col != 0:
                if str(list[n + row][m + col]) == neig:
                    count += 1
    for row in range(2):
        if str(list[n + row][m - 1]) == neig:
            count += 1
    return count


def neardown(list, n, m, neig):
    count = 0
    for row in range(2):
        for col in range(2):
            if row + col != 0:
                if str(list[n - row][m - col]) == neig:
                    count += 1
    for row in range(2):
        if str(list[n - row][m + 1]) == neig:
            count += 1
    return count


def nearleft(list, n, m, neig):
    count = 0
    for row in range(2):
        for col in range(2):
            if row + col != 0:
                if str(list[n + row][m + col]) == neig:
                    count += 1
    for col in range(2):
        if str(list[n - 1][m + col]) == neig:
            count += 1
    return count


def nearright(list, n, m, neig):
    count = 0
    for row in range(2):
        for col in range(2):
            if row + col != 0:
                if str(list[n + row][m - col]) == neig:
                    count += 1
    for col in range(2):
        if str(list[n - 1][m - col]) == neig:
            count += 1
    return count


def near(list, n, m, neig):
    count = 0
    for row in range(3):
        for col in range(3):
            if (row == 1) and (col == 1):
                pass
            else:
                if str(list[n - 1 + row][m - 1 + col]) == neig:
                    count += 1
    return count

s =[
    ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '#', '#', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]

pov = int(input())
for x in range(pov):
    s1 = []
    n = 0
    m = 0

    for x in range(len(s)):
        s1.append([])
        for i in range(len(s[0])):
            if m == 0 and n == 0:
                if s[n][m] == '.':
                    if near00(s, n, m, "#") == 3:
                        s1[n].append("#")
                    else:
                        s1[n].append(".")
                elif s[n][m] == '#':
                    if 2 <= near00(s, n, m, "#") <= 3:
                        s1[n].append("#")
                    else:
                        s1[n].append(".")
            elif m == len(s[0]) - 1 and n == 0:
                if s[n][m] == '.':
                    if near01(s, n, m, "#") == 3:
                        s1[n].append("#")
                    else:
                        s1[n].append(".")
                elif s[n][m] == '#':
                    if 2 <= near01(s, n, m, "#") <= 3:
                        s1[n].append("#")
                    else:
                        s1[0].append(".")
            elif m == 0 and n == len(s)-1:
                if s[n][m] == '.':
                    if near10(s, n, m, "#") == 3:
                        s1[n].append("#")
                    else:
                        s1[n].append(".")
                elif s[n][m] == '#':
                    if 2 <= near10(s, n, m, "#") <= 3:
                        s1[n].append("#")
                    else:
                        s1[n].append(".")
            elif m == len(s[0])-1 and n == len(s)-1:
                if s[n][m] == '.':
                    if near11(s, n, m, "#") == 3:
                        s1[n].append("#")
                    else:
                        s1[n].append(".")
                elif s[n][m] == '#':
                    if 2 <= near11(s, n, m, "#") <= 3:
                        s1[n].append("#")
                    else:
                        s1[n].append(".")
            elif n == 0:
                if s[n][m] == '.':
                    if nearup(s, n, m, "#") == 3:
                        s1[n].append("#")
                    else:
                        s1[n].append(".")
                elif s[n][m] == '#':
                    if 2 <= nearup(s, n, m, "#") <= 3:
                        s1[n].append("#")
                    else:
                        s1[n].append(".")
            elif n == len(s)-1:
                if s[n][m] == '.':
                    if neardown(s, n, m, "#") == 3:
                        s1[n].append("#")
                    else:
                        s1[n].append(".")
                elif s[n][m] == '#':
                    if 2 <= neardown(s, n, m, "#") <= 3:
                        s1[n].append("#")
                    else:
                        s1[n].append(".")
            elif m == len(s[0])-1:
                if s[n][m] == '.':
                    if nearright(s, n, m, "#") == 3:
                        s1[n].append("#")
                    else:
                        s1[n].append(".")
                elif s[n][m] == '#':
                    if 2 <= nearright(s, n, m, "#") <= 3:
                        s1[n].append("#")
                    else:
                        s1[n].append(".")
            elif m == 0:
                if s[n][m] == '.':
                    if nearleft(s, n, m, "#") == 3:
                        s1[n].append("#")
                    else:
                        s1[n].append(".")
                elif s[n][m] == '#':
                    if 2 <= nearleft(s, n, m, "#") <= 3:
                        s1[n].append("#")
                    else:
                        s1[n].append(".")
            elif (n >= 1 and n <= len(s) - 1) and (m >= 1 and m <= len(s[0]) - 1):
                if s[n][m] == '.':
                    if near(s, n, m, "#") == 3:
                        s1[n].append("#")
                    else:
                        s1[n].append(".")
                elif s[n][m] == '#':
                    if 2 <= near(s, n, m, "#") <= 3:
                        s1[n].append("#")
                    else:
                        s1[n].append(".")
            m += 1
        n += 1
        m = 0
    s = s1
for p in s:
    print(p)
