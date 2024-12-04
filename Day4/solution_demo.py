import regex as re

file = open("Day4/input_demo.txt", "r").read()

a1 = re.findall(r"XMAS", file, overlapped=True)
a2 = re.findall(r"SAMX", file, overlapped=True)
# S.{140}A.{140}M.{140}X.{140}|X.{139}M.{139}A.{139}S.{139}|S.{139}A.{139}M.{139}X.{139}|X.{141}M.{141}A.{141}S.{141}|S.{141}A.{141}M.{141}X.{141}", file, overlapped=True)
a3 = re.findall(r"X.{10}M.{10}A.{10}S", file, re.DOTALL, overlapped=True,)
a4 = re.findall(r"S.{10}A.{10}M.{10}X", file, re.DOTALL, overlapped=True)

a5 = re.findall(r"X.{9}M.{9}A.{9}S", file, re.DOTALL, overlapped=True)
a6= re.findall(r"S.{9}A.{9}M.{9}X", file, re.DOTALL, overlapped=True)

a7 = re.findall(r"X.{11}M.{11}A.{11}S", file, re.DOTALL, overlapped=True)
a8 = re.findall(r"S.{11}A.{11}M.{11}X", file, re.DOTALL, overlapped=True)




print(len(a1), len(a2), len(a3), len(a4), len(a5), len(a6), len(a7), len(a8))
print(len(a1) + len(a2) + len(a3) + len(a4) + len(a5) + len(a6) + len(a7) + len(a8))
