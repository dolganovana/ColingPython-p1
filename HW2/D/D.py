def solution(n,k):
    my_list = []
    c = 1
    count = 1
    t = True
    for i in range(1, n+1):
        my_list.append(c)
        c += 1

    if k == 1:
        final = n
    else:
        while t:
            for i in my_list:
                #print(i)
                if count == k:
                    #print(my_list, i)
                    if my_list.index(i) + 1 == len(my_list):
                        count = 1
                    else:
                        count = 2
                    my_list.remove(i)
                else:
                    count += 1

            if len(my_list) == 1:
                t = False



        final = my_list[0]

    return final
