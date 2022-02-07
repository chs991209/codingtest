import timeit


def solution_h(s):
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

print(timeit.timeit('solution_h("threezero123onethreezerothreezerothreezerothreezerothreezerothreezerothreezerothreezero1231threezerotwothreenineeight1one1zero3nine2five462")', number=1000, globals=globals()))

