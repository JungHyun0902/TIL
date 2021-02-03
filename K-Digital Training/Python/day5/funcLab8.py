def print_triangle_withdeco(a, b = '%'):
    if 1 <= a <= 10:
        for i in range(1, a+1):
            print(' '*(a-i), b*i)

print_triangle_withdeco(2)
print_triangle_withdeco(5, '*')
print_triangle_withdeco(11)
