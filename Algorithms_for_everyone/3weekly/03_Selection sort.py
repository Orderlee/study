def sel_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        max_idx = i  # min을 max로 변경
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:  # 부등호 방향 변경
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]

d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)
