def resolve():
    '''
    code here
    '''
    import collections
    H, W = [int(item) for item in input().split()]
    grid = [[item for item in input()] for _ in range(H)]

    stack = collections.deque()
    fp = [[0 for _ in range(W)] for _ in range(H)]

    start = False
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 's':
                start = [i, j] 
                break
        if start:
            break


    stack.append(start)
    is_found = False

    fp[start[0]][start[1]] = 1
    goto = [[1, 0], [0, 1], [-1, 0], [0, -1]]


    while stack:
        temp = stack.pop()
        y, x = temp
        # print(x,y)
        # print(grid[y][x])

        if grid[y][x] == 'g':
            is_found = True
            stack = False
        elif grid[y][x] == '#':
            pass
        else:
            for i in range(4):
                nx = x + goto[i][0]
                ny = y + goto[i][1]

                if 0 <= nx <= W-1 and 0 <= ny <= H-1:
                    if fp[ny][nx] == 0:
                        stack.append([ny, nx])
                        #.pop()中身が[y,x]だからここも揃える
                        fp[ny][nx] = fp[y][x] + 1
                        # print('next', nx, ny)

    print('Yes') if is_found else print('No')
            

if __name__ == "__main__":
    resolve()
