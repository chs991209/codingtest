import timeit
word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]


def solution(s):
    result = ""

    i = 0

    while i < len(s):
        if "0" <= s[i] <= "9":
            result += s[i]
            i += 1

        else:
            for k in range(10):
                if s.find(word[k], i, i+5) != -1:
                    result += str(k)
                    i += len(word[k])
                    break

    answer = int(result)

    return answer

print(timeit.timeit('solution("threezero123onethreezerothreezerothreezerothreezerothreezerothreezerothreezerothreezero1231threezerotwothreenineeight1one1zero3nine2five462")', number=1000, globals=globals()))
