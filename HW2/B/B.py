def solution(x):
    mystring = x
    newstring = ""
    for i in range(0, len(mystring)):
        if ((i == 0) or (i % 3 != 0)):
            if (mystring[i] == "h") and ((i != mystring.find("h")) or (i != mystring.rfind("h"))):
                newstring = newstring + "H"
            else:
                newstring = newstring + mystring[i]

    newstring = newstring.replace("1", "one")
    print(newstring)
    return
