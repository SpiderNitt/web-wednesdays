def string_compare(s1,s2):
    if len(s1) != len(s2):
        return False
    flag = True
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            flag = False
    return flag
