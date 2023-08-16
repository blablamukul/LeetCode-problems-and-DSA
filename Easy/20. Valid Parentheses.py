def isValid(s):
    slist=list(s)
    if len(slist)%2!=0:
        return False
    brack = {"{":"}", "[":"]", "(":")"}
    category = {"open": ["(", "{", "["], "close": [")", "}", "]"] }
    while True:
        if not slist:
            return True
        for i in range(len(slist)):
            if slist[0] in category["close"]:
                return False
            if slist[-1] in category["open"]:
                return False
            if slist[i] in category["close"]:
                openedIndex = category["open"].index(slist[i-1])
                if slist[i] == category["close"][openedIndex]:
                    slist.pop(i)
                    slist.pop(i-1)
                    break
                else:
                    return False

print(isValid("(())"))