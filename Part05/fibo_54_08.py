def multiply_2x2_matrices(A, B, m):
    C = [[0 for _ in range(2)] for _ in range(2)]
    C[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % m
    C[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % m
    C[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % m
    C[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % m
    print(C)
    return C


def fast_matrix_exponentiation(D, n, m):
    if n == 0:
        return [[1, 0], [0, 1]]
    if not n % 2:
        Z = fast_matrix_exponentiation(D, n // 2, m)
        return multiply_2x2_matrices(Z, Z, m)
    else:
        Z = fast_matrix_exponentiation(D, n // 2, m)
        Y = multiply_2x2_matrices(Z, Z, m)
        return multiply_2x2_matrices(Y, D, m)


def fibo_last_digit_modulo(n, m):
    M = [[0, 1], [1, 1]]
    P = fast_matrix_exponentiation(M, n, m)
    return P[0][1] % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibo_last_digit_modulo(n, m))
