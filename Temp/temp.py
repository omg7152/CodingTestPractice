import re
aaa = "100-200*300-500+20"

nums = list(map(str, re.split('[0-9]', aaa)))

print(nums)