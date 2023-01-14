def binary_search(keys, query):
    min_idx, max_idx, idx = 0, len(keys) - 1, 0
    while min_idx < max_idx:
        idx = (max_idx + min_idx) // 2
        print(query, keys, min_idx, max_idx, idx)
        if keys[idx] == query:
            return idx
        if keys[idx] < query:
            min_idx = idx + 1
        else:
            max_idx = idx - 1
    if keys[min_idx] == query:
        return min_idx
    return -1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
