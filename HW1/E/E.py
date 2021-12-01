def solution(x1, y1, x2, y2):
    
    check = False

    if abs(x2 - x1) < 2:
        if abs(y2 - y1) < 2:
            check = True
            
    return check
