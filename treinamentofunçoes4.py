def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [4, 8, 6, 0, 2]
dobra(valores)
print(valores)