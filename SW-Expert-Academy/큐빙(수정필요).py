import sys

input = sys.stdin.readline
u_list = [['w', 'w', 'w'] for i in range(3)]
d_list = [['y', 'y', 'y'] for i in range(3)]
l_list = [['g', 'g', 'g'] for i in range(3)]
r_list = [['b', 'b', 'b'] for i in range(3)]
f_list = [['r', 'r', 'r'] for i in range(3)]
b_list = [['o', 'o', 'o'] for i in range(3)]

cube_list = []
cube_list.append(u_list)
cube_list.append(d_list)
cube_list.append(l_list)
cube_list.append(r_list)
cube_list.append(f_list)
cube_list.append(b_list)


def rotation(what, dir):
    if what == 'U' or what == 'D':
        temp = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
        if what == 'U':
            row = 0
            if dir == '+':
                # 뒤 -> 오 -> 앞 -> 왼 (시계)
                index = [5, 3, 4, 2]
            else:
                # 뒤 -> 왼 -> 앞 -> 오 (반시계)
                index = [5, 2, 4, 3]
        else:
            row = 2
            if dir == '+':
                # 뒤 -> 왼 -> 앞 -> 오 (반시계)
                index = [5, 2, 4, 3]
            else:
                # 뒤 -> 오 -> 앞 -> 왼 (시계)
                index = [5, 3, 4, 2]
        for idx in range(len(index)):
            for i in range(3):
                if idx <= 2:
                    temp[idx+ 1][i] = cube_list[index[idx]][row][i]
                else:
                    temp[0][i] = cube_list[index[idx]][row][i]
        for idx in range(len(index)):
            for i in range(3):
                cube_list[index[idx]][row][i] = temp[idx][i]

    elif what == 'F' or what == 'B':
        temp = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
        if what == 'F':
            row = 2
            col = row - 2
            if dir == '+':
                # 윗 -> 오 -> 아 -> 왼 (시계)
                index = [0, 3, 1, 2]
            else:
                # 윗 -> 왼 -> 아 -> 오 (반시계)
                index = [0, 2, 1, 3]
        else:
            row = 0
            col = row
            if dir == '+':
                print('음')
                # 윗 -> 왼 -> 아 -> 오 (반시계)
                index = [0, 2, 1, 3]
            else:
                # 윗 -> 오 -> 아 -> 왼 (시계)
                index = [0, 3, 1, 2]

        for idx in range(len(index)):
            for i in range(3):
                if idx == 0:
                    temp[idx + 1][i] = cube_list[index[idx]][row][i]
                elif idx == 1:
                    temp[idx + 1][i] = cube_list[index[idx]][i][col]
                elif idx == 2:
                    temp[idx + 1][i] = cube_list[index[idx]][row][i]
                else:
                    temp[0][i] = cube_list[index[idx]][i][col+2]

        for idx in range(len(index)):
            for i in range(3):
                if idx % 2 == 0:
                    cube_list[index[idx]][row][i] = temp[idx][i]
                else:
                    if idx == 1:
                        cube_list[index[idx]][i][2 - row] = temp[idx][i]
                    else:
                        cube_list[index[idx]][i][row] = temp[idx][i]


    else:
        temp = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
        if what == 'L':
            col = 0
            if dir == '+':
                # 윗 -> 앞 -> 아 -> 뒤 (시계)
                index = [0, 4, 1, 5]
            else:
                # 윗 -> 뒤 -> 아 -> 앞 (반시계)
                index = [0, 5, 1, 4]
        else:
            col = 2
            if dir == '+':
                # 윗 -> 뒤 -> 아 -> 앞 (반시계)
                index = [0, 5, 1, 4]
            else:
                # 윗 -> 앞 -> 아 -> 뒤 (시계)
                index = [0, 4, 1, 5]

        for idx in range(len(index)):
            for i in range(3):
                if idx <= 2:
                    temp[idx + 1][i] = cube_list[index[idx]][i][col]
                else:
                    temp[0][i] = cube_list[index[idx]][i][col]
        for idx in range(len(index)):
            for i in range(3):
                cube_list[index[idx]][i][col] = temp[idx][i]

for tc in range(int(input())):
    print(tc)
    n = int(input())
    order = list(map(str, input().split()))
    for i in range(n):
        rotation(order[i][0], order[i][1])
        for i in range(3):
            for j in range(3):
                print(cube_list[0][i][j], end='')
            print()
        print()
    for i in range(3):
        for j in range(3):
            print(cube_list[0][i][j], end='')
        print()



