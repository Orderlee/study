def solve_maze(g, start, end):
    qu = []       # 기억 장소 1: 앞으로 처리해야 할 이동 경로를 큐에 저장
    done = set()  # 기억 장소 2: 이미 큐에 추가한 꼭짓점들을 집합에 기록(중복 방지)

    qu.append(start)  # 출발점을 큐에 넣고 시작
    done.add(start)   # 집합에도 추가

    while qu:
        p = qu.pop(0)
        v = p[-1]
        if v == end:
            return p
        for x in g[v]:
            if x not in done:
                qu.append(p + x)
                done.add(x)


    return "?"

maze = {
    'a': ['e'],
    'b': ['c', 'f'],
    'c': ['b', 'd'],
    'd': ['c'],
    'e': ['a', 'i'],
    'f': ['b', 'g', 'j'],
    'g': ['f', 'h'],
    'h': ['g', 'l'],
    'i': ['e', 'm'],
    'j': ['f', 'k', 'n'],
    'k': ['j', 'o'],
    'l': ['h', 'p'],
    'm': ['i', 'n'],
    'n': ['m', 'j'],
    'o': ['k'],
    'p': ['l']
}
print(solve_maze(maze, 'a', 'p'))