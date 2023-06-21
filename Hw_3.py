def dList(array: list[int]) -> list[int]:
    res = set()
    for el in array:
        counter = array.count(el)
        if counter > 1:
            res.add(el)
    return list(res)


print(dList([2, 2, 4, 5, 3, 8, 7, 8, 3, 3, 4, 1, 6, 9]))