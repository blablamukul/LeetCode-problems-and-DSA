def mergeTwoLists(list1, list2):
    newList = []
    list1copy = list(list1)
    list2copy = list(list2)
    for i in range(len(list1) if len(list1)<len(list2) else len(list2)):
        if list1[i]<list2[i]:
            newList.append(list1[i])
            list1copy.pop(0)
            newList.append(list2[i])
            list2copy.pop(0)
        else:
            newList.append(list2[i])
            list2copy.pop(0)
            newList.append(list1[i])
            list1copy.pop(0)
    if len(list1copy)==0:
        newList+=list2copy
    else:
        newList+=list1copy
    return newList

print(mergeTwoLists(list1 = [], list2 = []))