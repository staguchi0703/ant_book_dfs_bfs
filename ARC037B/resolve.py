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
            # print('temp',temp_node)
            # print('prev', prev)
            if next_edges != []:
                for next_node in next_edges:
                    # print('next', next_node)
                    if next_node != prev:
                        if fp[next_node] == 1:
                            is_roop = True
                            # print(is_roop)
                            pass
                        else:
                            stack.append([next_node, temp_node])


        return False if is_roop else True

    cnt = 0
    for i in range(1,N+1):
        # print('start', i)
        # print('-------')
        if fp[i] == 0:
            if dfs(i):
                cnt += 1
    print(cnt)

if __name__ == "__main__":
    resolve()
