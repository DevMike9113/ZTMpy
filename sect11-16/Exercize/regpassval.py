# at least 8 char long
# contain any sort of letters, numbers or symbols

import re

pw = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")

ent_pass = input("enter password:  ")

check = pw.fullmatch(ent_pass)

print(check)
