def fact(n: int):
    count = 1
    n_fact = 1
    while count <= n:
        if n % 2 == 0:
            for i in range(2, n + 1, 2):
                n_fact *= i
            break
        elif n % 2 != 0:
            n_fact *= count
            count += 2
    return n_fact


li_numb = [5, 6, 9, 12, 15]
for li_item in li_numb:
    print(fact(li_item))
