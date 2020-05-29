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



stack.append(start) #任意の開始ポイント
is_found = False

fp[start[0]][start[1]] = 1
goto = [[1, 0], [0, 1], [-1, 0], [0, -1]]


while stack:
    temp = stack.pop()
    y, x = temp

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

print('Yes') if is_found else print('No')

```



### [ATC 001 A 深さ優先探索](https://atcoder.jp/contests/atc001/tasks/dfs_a)

#### 方針

* ド定番
* 再帰で書く方が簡単だが、while文の方が変数のやり取りが分かりやすと感じた
* 本番でアレンジすることを考えてwhile文の書き方を習得しておく方がよさそう

``` python atc001a.py

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
```


### [ARC 031 B 埋め立て](https://atcoder.jp/contests/arc031/tasks/arc031_2)

#### 方針

* 全座標を対象にそこを`o`に変えたらどうなるか探索する
* 最初から`o`のところは1回だけ探索しておいてそれ以外は無視しても良いが、コードが複雑になりそうなため全部トライした。

#### 実装

* `copy.deepcopy()`を用いて毎回新しい盤面を用意した
* 探索済みの座標を'#'に塗り替えることで、最終番手後に一色となるように工夫した。
  * 後から考えると、'o'が残っていないを探索してもいいのでやり方は何でも構わないと気が付いた。

#### 解答


```python 

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

```

### [ARC037B バウムテスト](https://atcoder.jp/contests/arc037/tasks/arc037_b)

#### 方針

* 「木である　=　閉路がない」と読み替える
  * 閉路とは一度訪れたノードに再び訪れる経路があること
  * ただし、直前に訪れたノードへ帰る経路は無視する
  
#### 実装

* 直前に訪れたノードがどれかお覚えておくことが大事。
* 再帰関数で書けばどこから来たか一目瞭然なので問題ないが、while文では工夫が必要。
* 以下コードでは、stackに次のノードを積む際に現在ノードを次ノードの親としてセットした。
* `stack.append([next_node, temp_node])`

#### 解答

```python

def resolve():
    '''
    code here
    '''
    import collections

    N, M = [int(item) for item in input().split()]
    path_list = [[int(item) for item in input().split()] for _ in range(M)]

    edges = [[] for _ in range(N+1)]

    for a, b in path_list:
        edges[a].append(b)
        edges[b].append(a)

    stack = collections.deque()
    fp = [0 for _ in range(N+1)]

    def dfs(start):
        prev = -1
        stack.append([start, prev])

        is_roop = False
        while stack:
            temp_node, prev = stack.pop()
            next_edges = edges[temp_node]
            fp[temp_node] = 1

            if next_edges != []:
                for next_node in next_edges:
                    if next_node != prev:
                        if fp[next_node] == 1:
                            is_roop = True
                        else:
                            stack.append([next_node, temp_node])

        return False if is_roop else True

    cnt = 0
    for i in range(1,N+1):
        if fp[i] == 0:
            if dfs(i):
                cnt += 1
    print(cnt)

if __name__ == "__main__":
    resolve()

```

