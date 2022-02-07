import timeit


test2="""
resultanswer = output
"""

print(
    timeit.timeit(
        test2,
        setup="""
             
part = ["Marina", "josipa", "Eric", "Nikola", "Eric", "Vinko", "Filipa"]
completion = ["josipa", "Filipa", "Marina", "Eric", "Nikola", "Vinko"]
for p in part:
    if part.count(p) == 2:
        if completion.count(p) == 1:
            output = p
            break
    if part.count(p) == 1:
        if p not in completion:
            output = p
            break

""",
        number=1000000,
    )
)