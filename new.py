def sum_even_above_10(*num):
    total = 0
    for i in num:
        if i % 2 == 0 and i > 10:
            total += i
    return total
print(sum_even_above_10(10,20,20,10))

