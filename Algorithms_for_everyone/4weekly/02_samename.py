#딕셔너리: 정보를 찾는 기준이 되는 키(key)와 그 키에 연결된 값(value)의 대응 관계를 저장하는 자료 구조
# len(a) : 길이 구함
# d[key] : 딕셔너리 키값을 읽음
# d[key] = value : 키에 값을 저장
# del d[key] : 키에 해당값을 삭제
# clear() : 딕셔너리에 담긴 자료 지움
# key in d : 키가 딕셔너리 d 안에 있는지 확인
# s = st() : 빈 집합 s
# d = dict() : 빈 딕셔너리 / d.d = {} 도 같믐

def find_same_name(a):

    name_dict = {}
    for name in a:  #
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1


    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)

    return result

name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name))

name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name2))

