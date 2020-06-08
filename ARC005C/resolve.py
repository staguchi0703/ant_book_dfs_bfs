def resolve():
    '''
    code here
    '''

    import collections
    H, W = [int(item) for item in input().split()]
    grid = [[item for item in input()] for _ in range(H)]

    fp = [[-1 for _ in range(W)] for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if grid[i][j] == 's':
                start = [i, j]
            if grid[i][j] == 'g':
                goal = [i, j]


    que = collections.deque([[start[0], start[1], 0]])
    fp[start[0]][start[1]] = 0
    next_y_x = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    is_found = False

    while que:
        temp = que.popleft()

        if temp[0] == goal[0] and temp[1] == goal[1]:
            que = False
            is_found = True
        else:
            for dy, dx in next_y_x:
                ny = temp[0] + dy
                nx = temp[1] + dx

                if 0 <= ny <= H-1 and 0 <= nx <= W-1 and fp[ny][nx] == -1:
                    if grid[ny][nx] == '#': 
                        if temp[2] < 2:
                            que.append([ny, nx, temp[2]+1])
                            fp[ny][nx] = temp[2]+1
                    else:
                        que.appendleft([ny, nx, temp[2]])
                        fp[ny][nx] = temp[2]


    print('YES') if is_found else print('NO')


if __name__ == "__main__":
    resolve()


