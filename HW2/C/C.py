def solution(arr):
    newlist = []
    count = 1
    f = True
    while f:
        if count % 2 == 1:
            for i in arr[count]:
                newlist.append(i)

        f = False


    return newlist
