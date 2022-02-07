import timeit

test1 = """
resultanswer = output
"""

print(
    timeit.timeit(
        test1,
        setup="""
from collections import Counter
participant = ["Marina", "Josipa", "Nikola", "Vinko", "Filipa"]
completion = ["Josipa", "Filipa", "Marina", "Nikola"]
p_countdict = Counter(participant)
c_countdict = Counter(completion)
incomplete_dict = p_countdict - c_countdict
incomplete_name = list(incomplete_dict)[0]
if dict(p_countdict)[incomplete_name] == 2:
    output = incomplete_name
else:
    output = incomplete_name
""",
        number=1000000,
    )
)