import random

langs = ["Python",
        "Haskell",
        "Java",
        "Scala",
        "JavaScript",
        "C"
        "C++",
        "C#",
        ]


l = [random.random() * 1000000 for _ in range(250000)]

print(l[:18])