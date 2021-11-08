def solution(n,k):
    my_list = []
    c = 1
    count = 1
    t = True
    for i in range(1, n+1):
        my_list.append(c)
        c += 1

    while t:
        for i in my_list:
            #print(i, count)
            if count == k:
                my_list.remove(i)
                #print(i, count, my_list)
                count = 1 
            else:
                count += 1

        if len(my_list) == 1:
            t = False
    print(my_list)

    return my_list[0]
