
"""
o
t
f
s
e
n
0123456789
print(ord("o"))
print(ord("t"))
print(ord("f"))
print(ord("s"))
print(ord("e"))
print(ord("n"))
print(ord("0"))
print(ord("1"))
print(ord("2"))
print(ord("3"))
print(ord("4"))
print(ord("5"))
print(ord("6"))
print(ord("7"))
print(ord("8"))
print(ord("z"))
print(ord("a"))
"""

import timeit


def solution_h_1(s):
    submit = []
    f = 0
    while f < len(s):
        if "0" <= s[f] <= "9":
            submit.append(s[f])
            # 숫자 다음으로 -mv idx unit
            f += 1
            continue

        elif s[f] == "z":
            submit.append("0")
            f += 4
            continue

        elif s[f] == "o":
            submit.append("1")
            f += 3
            continue

        elif s[f] == "t":
            if s[f + 1] == "w":
                submit.append("2")
                f += 3
                continue

            elif s[f + 1] == "h":
                submit.append("3")
                f += 5
                continue

        elif s[f] == "f":
            if s[f + 1] == "o":
                submit.append("4")
                f += 4
                continue

            if s[f + 1] == "i":
                submit.append("5")
                f += 4
                continue

        elif s[f] == "s":
            if s[f + 1] == "i":
                submit.append("6")
                f += 3
                continue

            elif s[f + 1] == "e":
                submit.append("7")
                f += 5
                continue

        elif s[f] == "e" and s[f + 1] == "i":
            submit.append("8")
            f += 5
            continue

        elif s[f] == "n":
            submit.append("9")
            f += 4
            continue

    joinedtoint_submit = "".join(submit)
    return joinedtoint_submit

print(solution_h_1("threezero123onethreezerothreezerothreezerothreezerothreezerothreezerothreezerothreezero1231threezerotwothreenineeight1one1zero3nine2five462123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847"))
print(timeit.timeit('solution_h_1("threezero123onethreezerothreezerothreezerothreezerothreezerothreezerothreezerothreezero1231threezerotwothreenineeight1one1zero3nine2five462123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847")', number=1000, globals=globals()))


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

print(timeit.timeit('solution1("threezero123onethreezerothreezerothreezerothreezerothreezerothreezerothreezerothreezero1231threezerotwothreenineeight1one1zero3nine2five462123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847123132131232131231293847923874982374982739487923847")', number=1000, globals=globals()))

#
# def solution_h_2(s):
#     submit = []
#     f = 0
#     while f < len(s):
#         if "0" <= s[f] <= "9":
#             submit.append(s[f])
#             # 숫자 다음으로 -mv idx unit
#             f += 1
#             continue
#         elif "e" <= s[f] <= "z":
#             if s[f] == "z":
#                 submit.append("0")
#                 f += 4
#                 continue
#
#             elif s[f] == "o":
#                 submit.append("1")
#                 f += 3
#                 continue
#
#             elif s[f] == "t":
#                 if s[f + 1] == "w":
#                     submit.append("2")
#                     f += 3
#                     continue
#
#                 elif s[f + 1] == "h":
#                     submit.append("3")
#                     f += 5
#                     continue
#
#             elif s[f] == "f":
#                 if s[f + 1] == "o":
#                     submit.append("4")
#                     f += 4
#                     continue
#
#                 if s[f + 1] == "i":
#                     submit.append("5")
#                     f += 4
#                     continue
#
#             elif s[f] == "s":
#                 if s[f + 1] == "i":
#                     submit.append("6")
#                     f += 3
#                     continue
#
#                 elif s[f + 1] == "e":
#                     submit.append("7")
#                     f += 5
#                     continue
#
#             elif s[f] == "e" and s[f + 1] == "i":
#                 submit.append("8")
#                 f += 5
#                 continue
#
#             elif s[f] == "n":
#                 submit.append("9")
#                 f += 4
#                 continue
#         # else:
#         #     raise NotImplementedError
#
#     joinedtoint_submit = "".join(submit)
#     return joinedtoint_submit
#
#
# print(timeit.timeit('solution_h_2("threezero123onethreezerothreezerothreezerothreezerothreezerothreezerothreezerothreezero1231threezerotwothreenineeight1one1zero3nine2five462")', number=1000, globals=globals()))


# def solution_h_3(s):
#     submit = []
#     f = 0
#     while f < len(s):
#         if "0" <= s[f] <= "9":
#             submit.append(s[f])
#             # 숫자 다음으로 -mv idx unit
#             f += 1
#             continue
#
#         elif s[f] == "z":
#             submit.append("0")
#             f += 4
#             continue
#
#         elif s[f] == "o":
#             submit.append("1")
#             f += 3
#             continue
#
#         elif s[f] == "t":
#             if s[f + 1] == "w":
#                 submit.append("2")
#                 f += 3
#                 continue
#
#             elif s[f + 1] == "h":
#                 submit.append("3")
#                 f += 5
#                 continue
#
#         elif s[f] == "f":
#             if s[f + 1] == "o":
#                 submit.append("4")
#                 f += 4
#                 continue
#
#             if s[f + 1] == "i":
#                 submit.append("5")
#                 f += 4
#                 continue
#
#         elif s[f] == "s":
#             if s[f + 1] == "i":
#                 submit.append("6")
#                 f += 3
#                 continue
#
#             elif s[f + 1] == "e":
#                 submit.append("7")
#                 f += 5
#                 continue
#
#         elif s[f] == "e" and s[f + 1] == "i":
#             submit.append("8")
#             f += 5
#             continue
#
#         elif s[f] == "n":
#             submit.append("9")
#             f += 4
#             continue
#
#     joinedtoint_submit = "".join(submit)
#     return joinedtoint_submit
#
#
# print(timeit.timeit('solution_h_3("threezero123one")', number=1000, globals=globals()))
