def resolve():
    '''
    code here
    '''
    import collections
    H, W = [int(item) for item in input().split()]
    grid = [[item for item in input()] for _ in range(H)]

    fp = [[-1 for _ in range(W)] for _ in range(H)]

    que = collections.deque([[0, 0, 1]])
    fp[0][0] = 1
    next_y_x = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    is_found = False

    while que:
        temp = que.popleft()

        if temp[0] == H-1 and temp[1] == W-1:
            pass_num = temp[2]
            que = False
            is_found = True
        else:
            for dy, dx in next_y_x:
                ny = temp[0] + dy
                nx = temp[1] + dx

                if 0 <= ny <= H-1 and 0 <= nx <= W-1:
                    if grid[ny][nx] == '.' and fp[ny][nx] == -1:
                        que.append([ny, nx, temp[2]+1])
                        fp[ny][nx] = temp[2] + 1

    black_cnt = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                black_cnt += 1

    if is_found:
        print(H*W - black_cnt - pass_num)
    else:
        print(-1)


if __name__ == "__main__":
    resolve()
