def majority_element_naive(elements):
    srt_elements = sorted(elements)
    length = len(srt_elements)
    len_half = length // 2
    last_check = len_half + 1 if length % 2 else len_half
    for i in range(last_check):
        print(i, srt_elements)
        if srt_elements[i] == srt_elements[i + len_half]:
            return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))


"""
Naive solution:
def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

"""