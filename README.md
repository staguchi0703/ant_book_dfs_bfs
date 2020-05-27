# 蟻本2-1の中からDFSBFS

## 参考

* `https://qiita.com/drken/items/e77685614f3c6bf86f44`

* 上記に示される例題を解いた

## DFS

### DFS典型コード


* numpy.whereとか使いたくなるが、激重なので使用NG
* collection.queとlistのスライスで攻めるのが◎

```python dfs.py

import collections
H, W = [int(item) for item in input().split()]
grid = [[item for item in input()] for _ in range(H)]

stack = collections.deque()
fp = [[0 for _ in range(W)] for _ in range(H)]

# --------開始条件探索----------
start = False
for i in range(H):
    for j in range(W):
        if grid[i][j] == 's':
            start = [i, j] 
            break
    if start:
        break
#------------------------------

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
        # 探索終了条件
    elif grid[y][x] == '#':
        pass
        #障害物
    else:
        for i in range(4):
            nx = x + goto[i][0]
            ny = y + goto[i][1]

            if 0 <= nx <= W-1 and 0 <= ny <= H-1:
                if fp[ny][nx] == 0:
                    stack.append([ny, nx])
                    fp[ny][nx] = fp[y][x] + 1
                    # print('next', nx, ny)

print('Yes') if is_found else print('No')

    
```



### [ATC 001 A 深さ優先探索](https://atcoder.jp/contests/atc001/tasks/dfs_a)

