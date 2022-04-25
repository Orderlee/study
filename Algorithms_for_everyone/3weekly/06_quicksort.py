#그룹을 둘로 나눠 재귀호출 하는 바익은 병합 정렬과 같지만
#그룹을 나눌 떄 미리 기준과 비교해서 나눈다는 점이 다름

def bubble_sort(a):
    n = len(a)
    while True:  # 정렬이 완료될 때까지 계속 수행
        changed = False  # 자료를 앞뒤로 바꾸었는지 여부
        # 자료를 훑어 보면서 뒤집힌 자료가 있으면 바꾸고 바뀌었다고 표시
        for i in range(0, n - 1):
            if a[i] > a[i + 1]: # 앞이 뒤보다 크면
                print(a)        # 정렬 과정 출력(참고용)
                a[i], a[i + 1] = a[i + 1], a[i]  # 두 자료의 위치를 맞바꿈
                changed = True  # 자료가 앞뒤로 바뀌었음을 기록
        # 자료를 한 번 훑어보는 동안 바뀐 적이 없다면 정렬이 완성된 것이므로 종료
        # 바뀐 적이 있으면 다시 앞에서부터 비교 반복
        if changed == False:
            return

d = [2, 4, 5, 1, 3]
bubble_sort(d)
print(d)
