def solution(a, b):
    new = a.copy()
    for i in b:
        if i in a:
            continue
        else:
            new.append(i)

    new.sort()

    return new
