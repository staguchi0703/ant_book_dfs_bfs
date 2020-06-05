def resolve():
    '''
    code here
    pypy3で提出すればOK
    pythonはTLE
    '''
    import collections
    H, W = [int(item) for item in input().split()]
    grid = [[item for item in input()] for _ in range(H)]

    fp = [[-1 for _ in range(W)] for _ in range(H)]

    que = collections.deque()
    next_y_x = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    

    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                que.append([i, j, 0])
                fp[i][j] = 0

    while que:
        temp = que.popleft()

        for dy, dx in next_y_x:
            ny = temp[0] + dy
            nx = temp[1] + dx

            if 0 <= ny <= H-1 and 0 <= nx <= W-1:
                if fp[ny][nx] == -1:
                    que.append([ny, nx, temp[2]+1])
                    fp[ny][nx] = temp[2] + 1

    temp_max_list = []
    for line in fp:
        temp_max_list.append(max(line))

    print(max(temp_max_list))



if __name__ == "__main__":
    resolve()
