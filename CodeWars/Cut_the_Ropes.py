def cut_the_ropes(arr):
    count_list = []
    while arr:
        count_list.append(len(arr))
        arr = [a - min(arr) for a in arr]
        arr = [a for a in arr if a > 0]
    return count_list
    pass