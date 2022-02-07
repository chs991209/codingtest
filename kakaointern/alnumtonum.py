# ref : https://tech.kakao.com/2021/07/08/2021-%ec%b9%b4%ec%b9%b4%ec%98%a4-%ec%9d%b8%ed%84%b4%ec%8b%ad-for-tech-developers-%ec%bd%94%eb%94%a9-%ed%85%8c%ec%8a%a4%ed%8a%b8-%ed%95%b4%ec%84%a4/


"""
Instance object
-> s : 주어진 string class type의, 숫자로 변환 가능한 문자열
    __len__, __iter__, __next__ 등의 method를 자동 call 가능(하나의 function 내에서만 구현할 때는)
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
    '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
    '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
    '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__',
    '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
    '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
    'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
    'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
    'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
    'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
    'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
    'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper',
    'zfill']
    >> 필수적 : __contains__ : a in str(3) return bool
                __iter__, __getitem__ : __iter__이 존재하면 iterable한 객체로서 값을 이용해 명령을 순차적으로
                일정 단위마다 실행이 가능함
                __

    >> 문자열 str class의 method를 상속받은 string 객체들은,
    iterable하며, 따라서 문자열의 문자를 하나씩 numeric 한지, alphabet인지 등 도 구별해 가며 method로
    분석할 수 있다.
    따라서 주어진 문자열이

    alphabet
    numeric
    이 두 가지라면
    isalnum, isnum 만으로도 1차적으로 하나 하나 구분이 가능하다

    onetwothreefour2이어도,
    컴퓨터는 문자열의 알파벳 하나 하나도 전부 다른 객체로 보며, 연관성을 찾지 못하기 때문에
    1차적으로 숫자와 알파벳을 구분한 후,
    알파벳은 오름차순으로 읽어도 앞뒤의 연관성을 구분하지 못하므로

    구현하고자 하는 숫자로의 변환에 필요한,

    'one'이 있다면 'one'을 앞에서부터 읽을 때 컴퓨터는 어떻게, 어떤 걸 읽을 수 밖에 없는 지를 파악하여
    해당 step들을 조건화 하여, 1~9까지의 모든 숫자를 alphabet으로 나타낸 것을
    숫자를 나타내는 alphabet들의 큰 unit의 덩어리들로 분리하여, 간단하게 1~ 9 사이의 모든 step의 조건들에 대한
    각각의 숫자 값을 나타낼 수 있는 "숫자" string 값을 메모리에 쌓아, 가변형의 list에 append하면,
    또다시 iterable한 list에서 string 값들을 join하여 그 string 값 하나를 int로 형변환하면
    원하는 int 값을 return 할 수 있다.

    python에서 숫자를 불러오거나 return할 때 list를 활용하는 데에는,
    가변형이면서 중복에 의한 error 가 나지 않는 이유가 크다.



"""

# print(sorted(dir(str)))
# print()
# print()
# print(str.__getattribute__)


def solution1(s):
    answer = []
    f = 0
    while f < len(s):
        if "0" <= s[f] <= "9":
            answer.append(s[f])
            # 숫자 다음으로 -m idx unit
            f += 1

        elif s[f] == "z":
            answer.append("0")
            f += 4

        elif s[f] == "o":
            answer.append("1")
            f += 3

        elif s[f] == "t":
            if s[f + 1] == "w":
                answer.append("2")
                f += 3

            elif s[f + 1] == "h":
                answer.append("3")
                f += 5

            else:
                pass

        elif s[f] == "f":
            if s[f + 1] == "o":
                answer.append("4")
                f += 4

            if s[f + 1] == "i":
                answer.append("5")
                f += 4

            else:
                pass

        elif s[f] == "s":
            if s[f + 1] == "i":
                answer.append("6")
                f += 3

            elif s[f + 1] == "e":
                answer.append("7")
                f += 5

            else:
                pass

        elif s[f] == "e" and s[f + 1] == "i":
            answer.append("8")
            f += 5

        elif s[f] == "n":
            answer.append("9")
            f += 4

    joinedtoint_answer = int("".join(answer))
    return joinedtoint_answer


print(solution1("threezero123one"))

# mutable list에 str로 class type이 통일된 값을 append
# >> comprehension list 할당 proccess 제거, answer 재할당 선언 이전 list의 memory  remove
# return >> obj ->  list answer call>> str class의 method join call >> int() implement
# 가독성 고려 modification >> answer_joined = "".join(submit); answer_joined_toint = int(joined_submit)
# return answer_joined_toint
# print(ord("t"))
