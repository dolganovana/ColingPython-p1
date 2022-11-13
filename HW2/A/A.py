def solution(arr):
    maxim = 1
    count = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            count += 1
            if count > maxim:
                maxim = count
        else:
            count = 1

    return maxim
