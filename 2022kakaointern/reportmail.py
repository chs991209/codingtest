# 문제 1 – 신고 결과 받기
# 정답률 : 80.13%
# 문제 1 풀러가기
# 문제 설명
# 신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.
#
# 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
#
# 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.   ->>> 가변성 객체
# 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.   ->>> 횟수값 중복 없음. 결과를 True/False로 구분 가능
# k번 이상 신고된 유저는 즉시 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
# 게시판 이용이 정지된 유저도 불량 이용자를 신고할 수 있습니다.


"""
-> "신고자"가 "불량 이용자"를 1번씩 "n"번 신고하였다. "n"번 신고한 결과는 "신고 결과"이다.
"신고자", "불량 이용자"는 param으로, 인정 신고 횟수는 "n"회로 누적하고 , "신고 결과": if n >= k: 정지 = True(또는 1), else: 정지 = False(,None or 0)이다.
"신고 결과"에 상관없이 "신고자"로서 "불량 이용자"를 여러 번 신고할 수 있다.
따라서 “muzi”는 처리 결과 메일을 2회, “frodo”와 “apeach”는 각각 처리 결과 메일을 1회 받게 됩니다.

이용자의 id가 담긴 문자열 배열 id_list, 각 이용자가 신고한 이용자에 대한 정보가 담긴 문자열 배열 report,
정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때, 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해 주세요.



함수는 "게시판"의 신고 시스템, "신고 시스템의 결과"를 "메일로 발송"하는 시스템이 다룬 값을 최종 output 값을 return하게 한다.

Param group; 1  -- "신고자"가 "불량 이용자"를 "n번" (신고)하는 시스템. (신고)는 "신고자", "불량 이용자"를 인자로 받고,
"신고자 모임"이라는 가변형 객체와 "n"번이라는 값을 누적함(고정 복잡도의 덧셈연산자)

(신고)는 누적된 "n" 값, "신고자 모임" 을 return하고, (정지)는 "신고자 모임" 가변형 객체, "불량 이용자"를 그대로 이어서 받음. (신고는)

Param group; 2  -- "n"번 이상 신고된 "불량 이용자"가 (정지)되는 시스템. (정지)는 누적된 "n"값을 그대로 이어서 받고(값을 그대로 내려받음)

------------------------------------
            id_list                                     report                                  k	            result
            -------                           ----["신고자 불량 이용자"]----                   ---"상수"----   --"신고 결과, 신고 결과, .."---
["muzi", "frodo", "apeach", "neo"]      	["muzi frodo","apeach frodo","frodo neo",           2          	  [2,1,1,0]
                                                "muzi neo","apeach muzi"]
  인자(받았을 때 o(n) 이상 검열, 불변형)            인자(o(n) str __iter__검열)                   인자(o(1))       누적(o(n))
                                             id_list와 문자열 값의 종류가 일부 같음
"""

import timeit

"""
2 ≤ id_list의 길이 ≤ 1,000
1 ≤ id_list의 원소 길이 ≤ 10
id_list의 원소는 이용자의 id를 나타내는 문자열이며 알파벳 소문자로만 이루어져 있습니다.
1 ≤ report의 길이 ≤ 200,000
3 ≤ report의 원소 길이 ≤ 21
report의 원소는 “이용자 id 신고 id”형태의 문자열입니다.
예를 들어 “muzi frodo”의 경우 “muzi”가 “frodo”를 신고했다는 의미입니다.
id는 알파벳 소문자로만 이루어져 있습니다.
이용자 id와 신고 id는 공백(스페이스) 하나로 구분되어 있습니다.
자기 자신을 신고하는 경우는 없습니다.
1 ≤ k ≤ 200, k는 자연수
return 하는 배열은 id_list에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 담으면 됩니다.
"""

id_list1 = ["apeach", "frodo", "muzi", "neo"]
report1 = [
    "muzi frodo",
    "apeach frodo",
    "frodo neo",
    "muzi neo",
    "apeach muzi",
    "apeach muzi",
]
k = 2
# 검열
# 정지된 사람, 신고한 사람 모두에게 메일을 발송


def sentmailcount(id_list, report, k):
    """
    id_list의 원소는 각각 name으로,
    str class>> name을 그대로 하나씩 읽어서
    report의 str class>>name pair에 존재하는 지를 확인하고, k번 이상 다른 name으로부터 신고를 받은 latter name의 신고 횟수(int)와 신고한 횟수(int) 를 합하여 각각
    result에 담고 빠져나와 return한다.
    만약 신고가 들어올 때마다 신고 횟수를 누적하고 메일 발송 횟수까지 누적하는 closure 함수를 만든다면?
    >> 실무에 활용
    :using method : split(), index(), add(a, b)
    :param id_list, report, k:
    :return: result
    """
    deathnote = [0 for k in id_list]  # 신고 먹은 횟수 list
    reporter = [0 for k in id_list]  # 성공적 신고자 신고 횟수 list
    result = []  # 메일 발송 list

    # 신고가 들어온다
    # 그렇다면, 신고를 누적해 준다. dict에
    # 반복
    # 신고가 k회 이상 되면,
    # dict의 key를 원래의 id 값으로 다시 선언해 준다.
    # 신고된 사람을 누적해 주는 dict에서, 방금 다시 선언해준 key에 맵핑된 value에 True를 선언해 준다.
    #
    # True로 바뀐 dict는 다른 data 자료형과 함께 db에 저장된다. db는 정지 여부를 판별하는
    # 코드에서 선언되며, 이때 이후로 정지 여부가 함께 패치된다.
    #

    # DB의 생성 과정

    # 전체 Userlist

    # User의 정지 True/False 값을 가진 UserList(dict가 원소)

    # Userlist에 추가되는 username은 dict가 원소인 UserList에 접근해 새로운 key값이 username이며, key 값이 전부 False인 dict를 생성하며
    # list에 접근한다.

    # 신고 횟수를 누적한 value를 key로 가진 dict를 포함한, DB 속의 list에 접근하면서
    # key 값은 username, value는 전부 0의 값을 가진 dict를 생성하며 list의 원소로 만들어 접근한다.
    # 실제 Db는 [{"username": "Kim", "Ban": "False"}, {"username": "Lee", "Ban": "False"}, ..]

    # print(result)
    # def fucn() 구현하고, 안의 variable의 값을 클로저 실행하고, 마지막 값을 특정 기간에 return하면 특정 기간에 클로저로 완성된 데이터를 얻으면,
    # time 관련 메소드 등을 데이터 얻는 함수에서 같이 실행해서 분석할 수도 있다
    # time 관련 메소드는 decorator 등으로 간단히 필요한 곳에 작성
    for name in id_list:

        # sorted() Method

        for namepair in sorted(list(set(report))):  # 신고 내역을 하나씩 조사
            # split() Method

            if name in namepair.split():  # 어피치의 이름에 대해 신고 내역을 하나씩 조사해 보자
                if namepair.split().index(name) == 1:  # 만약 어피치의 이름이 신고 대상에 기록되었을 때
                    # --> deathnote
                    deathnote[id_list.index(name)] += 1  # 데스노트 리스트 = deathnote += 1
                    # print("{}가 신고받은 내역을 방금 처리했습니다 + 1, 현재 {}번 경고".format(name, deathnote[id_list.index(name)]))
                    # print("The warning counted as : {}".format(deathnote))
                    # print()

    i = 0
    while i < len(id_list):
        if deathnote[i] >= k:
            baduser = id_list[i]
            for script in sorted(list(set(report))):
                if script.split()[1] == baduser:
                    # print(baduser)
                    reporter[id_list.index(script.split()[0])] += 1

        i += 1

    for i in range(len(id_list)):
        n = 0
        if deathnote[i] >= k:
            n = 1
        result.append(n + reporter[i])

    return result


# print(id_list1)
# print("The result is", sentmailcount(id_list1, report1, k))


print(
    timeit.timeit("sentmailcount(id_list1, report1, k)", number=1000, globals=globals())
)
print(sentmailcount(id_list1, report1, k))


# 신고한 유저에게만 메일 발송
def sentmailcount_1(id_list, report, k):
    """
    id_list의 원소는 각각 name으로,
    str class>> name을 그대로 하나씩 읽어서
    report의 str class>>name pair에 존재하는 지를 확인하고, k번 이상 다른 name으로부터 신고를 받은 latter name의 신고 횟수(int)와 신고한 횟수(int) 를 합하여 각각
    result에 담고 빠져나와 return한다.
    만약 신고가 들어올 때마다 신고 횟수를 누적하고 메일 발송 횟수까지 누적하는 closure 함수를 만든다면?
    >> 실무에 활용
    :using method : split(), index(), add(a, b)
    :param id_list, report, k:
    :return: result
    """

    deathnote = [0 for n in id_list]  # 신고 먹은 횟수 list
    result = [0 for n in id_list]  # 메일 발송 list

    for name in id_list:

        # sorted() Method

        for namepair in sorted(list(set(report))):  # 신고 내역을 하나씩 조사
            # split() Method

            if name not in namepair:
                continue

            elif (
                name in namepair.split() and namepair.split().index(name) == 1
            ):  # 만약 어피치의 이름이 신고 대상에 기록되었을 때
                # --> deathnote
                deathnote[id_list.index(name)] += 1  # 데스노트 리스트 = deathnote += 1

    i = 0
    while i < len(id_list):
        if deathnote[i] >= int(k):
            baduser = id_list[i]
            for script in sorted(list(set(report))):
                if script.split()[1] == baduser:
                    # print(baduser)
                    result[id_list.index(script.split()[0])] += 1

        i += 1

    return result


print(
    timeit.timeit(
        "sentmailcount_1(id_list1, report1, k)", number=1000, globals=globals()
    )
)
print(sentmailcount_1(id_list1, report1, k))


# 신고한 유저에게만 메일 발송
def sentmailcount_dict(id_list, report, k):
    """
    id_list는 원소의 중복이 없는 list이며,
    신고 내역 list에서 신고자: [신고한 사람들] 구조로 dict를 setdefault를 이용해 생성한다.
    setdefault를 통해 생성한 신고된 유저 dict의 value의 len이 k 이상일 때,
    value list를 풀어내,
    id_list와 맵핑된 count numbers에 0에서 call될 때마다 1을 추가한다.
    추가 완료 후 list를 return한다.
    :param id_list, report, k:
    :return: result
    """

    reportpair = {}  # 신고 userid 기록 dict
    result = [0 for n in id_list]  # 메일 발송 list, index를 id_list와 동일하게 배치한다.

    reportpairlist = (j.split() for j in (set(report)))

    for reporter, baduser in reportpairlist:
        reportpair.setdefault(baduser, []).append(reporter)

    # for baduser, reporter in reportpair.items():
    for reporter in reportpair.values():
        if len(reporter) >= k:
            for i in reporter:
                result[id_list.index(i)] += 1

    return result


print(
    timeit.timeit(
        "sentmailcount_dict(id_list1, report1, k)", number=1000, globals=globals()
    )
)

print(sentmailcount_dict(id_list1, report1, k))
