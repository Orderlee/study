#완주하지 못한 선수
# def solution(participant,completion):
#
#     for i in participant:
#         if participant.count(i)-completion.count(i):
#             return i
#
#
#
# print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
# print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))



# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#
#     for i in range(len(participant)):
#         if participant[i] != completion[i]:
#             #print(participant)
#             return participant[i]
#     return participant[-1]
#
# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]
# print(solution(participant,completion))

#전화번호 목록
# def solution(phone_book):
#     answer = True
#     for i in range(len(phone_book)):
#         l = len(phone_book[i])
#         for j in range(i+1, len(phone_book)):
#             l2 = len(phone_book[j])
#             if l != l2:i
#                 answer=False
#     return answer
#
#
# print(solution(["119", "97674223", "1195524421"]))
# print(solution(["123","456","789"]))
# print(solution(["12","123","1235","567","88"]))

#위장
# def solution(clothes):
#     answer = 0
#     return answer
#
#
# print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
# print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))





#