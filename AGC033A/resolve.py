def resolve():
    '''
    code here
    '''
    import collections
    H, W = [int(item) for item in input().split()]
    grid = [[item for item in input()] for _ in range(H)]
    que = collections.deque()
    next_y_x = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    res = 0

    is_not_all_black = False
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':
                is_not_all_black = True
                break
        else:
            if is_not_all_black:
                break

    
    while is_not_all_black:
        res += 1
        is_not_all_black = False
        for i in range(H):
            for j in range(W):
                if grid[i][j] == '#':
                    que.append([i, j])
                else:
                    is_not_all_black = True

        while que:
            temp = que.popleft()

            for dy, dx in next_y_x:
                ny = temp[0] + dy
                nx = temp[1] + dx

                if 0 <= ny <= H-1 and 0 <= nx <= W-1:
                    if grid[ny][nx] == '.':
                        grid[ny][nx] = '#'


    print(res-1)

if __name__ == "__main__":
    resolve()
