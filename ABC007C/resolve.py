def resolve():
    '''
    code here
    '''
    import collections

    R, C = [int(item) for item in input().split()]
    sy, sx = [int(item) for item in input().split()]
    gy, gx = [int(item) for item in input().split()]

    grid = [[item for item in input()] for _ in range(R)]

    fp = [[-1 for _ in range(C)] for _ in range(R)]

    res = 0
    que = collections.deque([[sy-1, sx-1, 0]])
    fp[sy-1][sx-1] = 0

    d_y_x_list = [[1, 0], [0, 1], [-1, 0,], [0, -1]]

    while que:
        y, x, cnt = que.popleft()

        if y == gy-1 and x == gx-1:
            res = cnt
            que = False

        else:
            for dy, dx in d_y_x_list:
                ny = y + dy
                nx = x + dx

                if 0 <= ny <= R-1 and 0 <= nx <= C-1:
                    if grid[ny][nx] != "#" and fp[ny][nx] == -1:
                        que.append([ny, nx, cnt + 1])
                        fp[ny][nx] = cnt + 1
                        # print(ny, nx, cnt + 1)

    print(res)


if __name__ == "__main__":
    resolve()

