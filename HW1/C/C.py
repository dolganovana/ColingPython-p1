def solution(n, k):
    result = k//n
    ostatok = k - n * result
    print(result, ostatok)
    return
