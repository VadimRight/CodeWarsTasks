def cut_the_ropes(arr):
    count_list = []
    while arr:
        count_list.append(len(arr))
        min_length = min(arr)
        arr = [a - min_length for a in arr if a > min_length]
    return count_list
