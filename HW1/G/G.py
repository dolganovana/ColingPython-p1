def solution(a, b):
    
     unite = b.copy()
     print(unite)

    for i in a:
        if not (i in b):
            print(i)
            unite.append(i)

    unite.sort()
    print(unite)

    return
