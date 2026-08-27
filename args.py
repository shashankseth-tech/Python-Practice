def above_10(*args):
    result = []
    for i in args:
        if i > 10:
         result.append(i)
    return result
print(above_10(10,20,30,40))
