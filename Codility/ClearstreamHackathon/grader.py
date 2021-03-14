#!/bin/env python
import sys
import importlib
from datetime import datetime

test = __import__(sys.argv[1])


print("H MIN SEC\n\n")
for i in sys.argv[2:]:
    now = datetime.now()
    params = test.gen(int(i))
    #print("PARAMS:", params)
    if type(params) is tuple:
        test.solution(*params)
        print(
            "ANSWER:",
            datetime.now() - now,
            "\n",
        )
    else:
        test.solution(params)
        print(
            "ANSWER:",
            datetime.now() - now,
            "\n",
        )