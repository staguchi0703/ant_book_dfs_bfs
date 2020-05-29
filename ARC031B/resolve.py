def resolve():
    '''
    code here
    '''
    import copy
    import collections
    grid = [[item for item in input()] for _ in range(10)]

    is_found = False

    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'o':
                start = [i, j]
                is_found = True
                break
        if is_found:
            break

    def dfs(grid, start):
        stack = collections.deque([start])
        is_found = False

        goto = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while stack:
            temp = stack.pop()
            y, x = temp
            grid[y][x] = 'x'
            # print(x,y)
            # print(grid[y][x])

            for i in range(4):
                nx = x + goto[i][0]
                ny = y + goto[i][1]

                if 0 <= nx <= 9 and 0 <= ny <= 9:
                    if grid[ny][nx] == 'o':
                        stack.append([ny, nx])
                        #.pop()中身が[y,x]だからここも揃える
                        grid[ny][nx] = 'x'
                        # print('next', nx, ny)
    
        for i in range(10):
            for j in range(10):
                if grid[i][j] != 'x':
                    # print(grid[i][j])
                    return False
        return True

    is_slove = False

    for i in range(10):
        for j in range(10):
            temp_grid = copy.deepcopy(grid)
            temp_grid[i][j] = 'o'
            # print(j, i)
            if dfs(temp_grid, start):
                # print(j,i)
                is_slove = True
                break
        if is_slove:
            break

    print('YES') if is_slove else print('NO')
            

if __name__ == "__main__":
    resolve()
