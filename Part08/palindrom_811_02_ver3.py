def lps(source: str):
    length = len(source)
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
a -> a
ab -> a
abb -> bb
aab -> aa
bmanchdaem -> manam
meadhcnamb -> madam
bmadnchdaem -> madndam
meadhcndamb -> madhdam
dgdcgdhhddhgaehbbbce -> chhddhhc
ecbbbheaghddhhdgcdgd -> chhddhhc
dgdcgdhhdd -> ddhhdd
ddhhdgcdgd -> ddhhdd
abcdefgh -> a
hgfedcba -> h
"""