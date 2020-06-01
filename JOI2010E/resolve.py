def resolve():
    '''
    code here
    '''
    import collections
    H, W , N = [int(item) for item in input().split()]
    grid = [[item for item in input()] for _ in range(H)]

    def find_pos(S):
        is_found = False
        for i in range(H):
            for j in range(W):
                if S == 0:
                    if grid[i][j] == 'S':
                        sy = i
                        sx = j
                        is_found = True
                        return sy, sx
                else:
                    if grid[i][j] == str(S):
                        sy = i
                        sx = j
                        is_found = True
                        return sy, sx


    def path_num(start, goal):
        sy, sx = find_pos(start)
        gy, gx = find_pos(goal)
        que = collections.deque([[sy, sx, 0]])
        fp = [[-1 for _ in range(W)] for _ in range(H)]
        d_y_x_list = [[1, 0], [0, 1], [-1, 0,], [0, -1]]

        while que:
            y, x, cnt = que.popleft()

            if y == gy and x == gx:
                return cnt

            else:
                for dy, dx in d_y_x_list:
                    ny = y + dy
                    nx = x + dx

                    if 0 <= ny <= H-1 and 0 <= nx <= W-1:
                        if grid[ny][nx] != "X" and fp[ny][nx] == -1:
                            que.append([ny, nx, cnt + 1])
                            fp[ny][nx] = cnt + 1
                            # print(ny, nx, cnt + 1)
        

    res = 0
    for num in range(N):
        res += path_num(num, num+1)

    print(res)


if __name__ == "__main__":
    resolve()
