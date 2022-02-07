import timeit



test1="""
soluted_answer = answer
"""

print(
    timeit.timeit(
        test1,
        setup="""
s = "threezero123one"
answer = []
i = 0
while i < len(s) :
    if s[i] == 'z':
        answer.append(0)
        i += 4
    elif s[i] == 'o':
        answer.append(1)
        i += 3
    elif s[i] == 't' and s[i+1] == 'w':
        answer.append(2)
        i += 3
    elif s[i] == 't' and s[i+1] == 'h':
        answer.append(3)
        i += 5
    elif s[i] == 'f' and s[i+1] == 'o':
        answer.append(4)
        i += 4
    elif s[i] == 'f' and s[i+1] == 'i':
        answer.append(5)
        i += 4
    elif s[i] == 's' and s[i+1] == 'i':
        answer.append(6)
        i += 3
    elif s[i] == 's' and s[i+1] == 'e':
        answer.append(7)
        i += 5
    elif s[i] == 'e' :
        answer.append(8)
        i += 5
    elif s[i] == 'n' :
        answer.append(9)
        i += 4
    elif '0' <= s[i] <= '9' :
        answer.append(s[i])
        i += 1
answer = [str(int) for int in answer]
answer = "".join(answer)
answer = int(answer)
""",
        number=1000000,
    )
)


