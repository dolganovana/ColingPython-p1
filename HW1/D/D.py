def solution(total):
    total2 = total % 1440
    hours = total2 // 60
    minutes = total2 % 60
    
    return str(hours) + ' ' + str(minutes)
