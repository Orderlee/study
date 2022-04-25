#회문: 순서대로 읽어도 거꾸로 읽어도 내요이 같은 낱말이나 문장
#큐(queue): 줄서기에 비유, 가장 먼저 줄을 선 사람이 가장 먼저 택시를 탐 (First In First Out)
#인큐(enqueue): 큐에 자료를 넣는 동작
#디큐(dequeue): 큐에 자료를 꺼내는 동작
#스택: 접시 쌓기에 비유, 가장 마지막에 들어간 자료를 가장 먼저 꺼내는 것 (Last In First Out)


def palindrome(s):

    qu = []
    st = []

    for x in s:

        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())

    while qu:
        if qu.pop(0) != st.pop():  #
            return False

    return True

print(palindrome("Wow"))
print(palindrome("Madam, I’m Adam."))
print(palindrome("Madam, I am Adam."))
