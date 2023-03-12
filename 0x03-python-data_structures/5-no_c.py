#!/usr/bin/python3
def no_c(my_string):
    ans = ""
    for x in my_string:
        if x.__eq__("c") | x.__eq__("C"):
            continue
        else:
            ans += x
    return ans
