import re

pattern2 = re.compile(r"([a-zA-Z]).([a])")
pattern = re.compile(
    r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+["
    r"a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
)

string = 'andrei'

aa = pattern.search(string)
# bb = pattern.findall(string)
# cc = pattern.fullmatch(string)
# dd = pattern.match(string)
# print(aa)
# print(bb)
# print(cc)
# print(dd)

# a = re.search(string)
# print(a.span())
# print(a.start())
# print(a.end())
print(aa)

# ---------

# regex
