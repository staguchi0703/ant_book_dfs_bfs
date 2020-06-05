# 蟻本2-1の中からDFSBFS

## 参考

* `https://qiita.com/drken/items/e77685614f3c6bf86f44`

* 上記に示される例題を解いた

## DFS

### DFS典型コード


* numpy.whereとか使いたくなるが、激重なので使用NG
* collection.queとlistのスライスで攻めるのが◎

```python

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

```

## BFS

### BFSの典型コード

```python

import collections
H, W = [int(item) for item in input().split()]
grid = [[item for item in input()] for _ in range(H)]

fp = [[-1 for _ in range(W)] for _ in range(H)]

# position[y, x]
# start [0,0]
# goal [H-1, W-1]

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

print(pass_num) if is_found else print(-1)
```

### [ABC007 幅優先探索](https://atcoder.jp/contests/abc007/)

#### 方針

* 典型的なBFS

#### 実装

* 使いまわせるように工夫した
* 足跡を記録するfp配列
  * -1で初期化
  * 開始地点を0で初期化
  * que追加の際に足跡を記録
* 行先を`d_y_x_list`として登録することで、他の方向で動いても対応可
* 入れる値受ける値を配列のスライス順に合わせてy,xの順序で処理してた
* 次の番手目が分かるようにqueに次の番手目を加えた
* 次の番手目が枠をはみ出しているか判定するために、`ny, nx`を計算し、if文で絞り込みをかけた 


### [JOI2010 E](https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e)

### 方針

* 繰り返し計算するので、始点・終点探しと探索を関数化した。

### 実装

 * 工夫はない

```python

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

```


### [ABC088D - Grid Repainting](https://atcoder.jp/contests/abc088/tasks/abc088_d)

#### 方針

* 黒く塗っても最短経路でゴールできる場合が解になる
* ゴールした経路を求めて、それ以外を黒塗ればいい
    * 問われているのは個数だから正確なルート座標は分からなくてもいい
    * 最短経路の手数さえわかればよい
* もともと黒い所は色が変えられないのだから点数にならない
* よって解は「全マス数　-　最短経路の手数　-　もともと黒の個数」となる

#### 実装

* 普通にBFSで最短経路の手数求めただけ
* 答えが見つからない場合もあるので、ゴールが見つかったときに`is_found　= True`にする。

```python

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

```

### [AGC033A](https://atcoder.jp/contests/agc033/tasks/agc033_a)

* pypy3でクリア