import regex as re

file = open("Day4/input.txt", "r").read()

a1 = re.findall(r"[M].[M].{139}[A].{139}[S].[S]|[M].[S].{139}[A].{139}[M].[S]|[S].[M].{139}[A].{139}[S].[M]|[S].[S].{139}[A].{139}[M].[M]", file, re.DOTALL, overlapped=True)




print(len(a1))
