#순차 탐색:리스트 안에 있는 원소를 하나씩 순차적으로 비교하면서 탐색한다

def search_list(a,x):
    n = len(a)
    result = []
    for i in range(0,n):
        if x ==a[i]:
            result.append(i)
    return result

a  =[2, 10, 33, 50, 100]

print(search_list(a, 10))
print(search_list(a,100))

## 복잡도는 O(n)이다

