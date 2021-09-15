def solution(n):
    
    stepeni = []
    stepen = 1
    
    while stepen <= n:
        stepeni.append(stepen)
        stepen = stepen * 2

    print(stepeni)

    return
