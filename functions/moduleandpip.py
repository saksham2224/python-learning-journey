# we can use pre wwritten codes wwritten by somebody else using modules
'''twwo types of moduls in python
- Built in module
- External Module
'''
import math

import mymodule
import requests # type: ignore

print(math.sqrt(9))
mymodule.hello()

r = requests.get("https://www.google.com")
print(r.text)