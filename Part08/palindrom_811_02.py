def lps(source: str):
    length = len(source)
    if length == 2 or length == 3:
        if source[0] != source[-1]:
            return source[0]
        else:
            return source
    for distance in range(length - 1, 0, -1):
        for left in range(0, length - distance):
            right = left + distance
            # print(source)
            # print(length, distance, left, right)
            if distance == 1 and source[left] == source[right]:
                return source[left] + source[right]
            if source[left] == source[right]:
                return source[left] + lps(source[left + 1: right]) + source[right]
    # print(f"source: {source}")
    return source[0]


if __name__ == '__main__':
    print(lps(input()))

"""
0123456789
bmanchdaem
dgdcgdhhddhgaehbbbce
dgdcgdhhdd
abcdefgh
"""