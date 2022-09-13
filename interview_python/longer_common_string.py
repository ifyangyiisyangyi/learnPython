# 最大公共子串
def longer_common_string(a, b):
    f = []
    for i in range(1, len(a) + 1):
        for j in range(len(a) + 1 - i):
            e = a[j:j+i]
            if e in b:
                f.append(e)
    print(f)
    return f[-1]

if __name__ == '__main__':
    a = "abjeccarde"
    b = "sjdgcargde"
    res = longer_common_string(a, b)
    print(res)