def what_time_is_it(angle):
    h = angle // 30
    m = angle % 30 * 2
    if h == 0:
        h = 12
    return '{:02d}:{:02d}'.format(h, m)