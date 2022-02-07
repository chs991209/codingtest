import timeit


test1="""
soluted_answer = joined_answer
"""

print(
    timeit.timeit(
        test1,
        setup="""
s = "threezero123one"
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

joined_answer = int("".join(answer))

""",
        number=1000000,
    )
)


