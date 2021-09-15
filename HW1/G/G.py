def solution(a, b):
    
     unite = a.copy()
     print(unite)

    for i in b:
        if not (i in a):
            print(i)
            unite.append(i)

    unite.sort()
    print(unite)

    return
