# ---------- STRING CONCATENATION --------------
# CONCATINATION IS A PROCESS OS COMBINING TWO OR MORE STRINGS into a single using "+"

def concatenate(s1: str, s2: str) -> str:
    s3 = s1 + s2
    if len(s3) > 10:
        return "Too long!"
    return s3


print(concatenate("He", "llo"))
print(concatenate("Hello", "world!"))
print(concatenate("Length", "of10"))
print("-----")

