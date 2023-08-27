def containsDuplicate(nums):
    elementCount = {}
    for i in nums:
        if i not in elementCount:
            elementCount[i]=1
        else:
            return True
    return False

print(containsDuplicate([94,988,38,-369,409,-559,-529,-298,-593,705])) 