import re

pattern = re.compile(r"([a-zA-Z]).([a])")

string = 'search inside this text'

aa = pattern.search(string)
bb = pattern.findall(string)
cc = pattern.fullmatch(string)
dd = pattern.match(string)
print(aa)
print(bb)
print(cc)
print(dd)

# a = re.search(string)
# print(a.span())
# print(a.start())
# print(a.end())
print(aa.group(1))

# ---------

# regex
