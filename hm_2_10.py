n = int(input())
one = zero = 0
for i in range(n):
    x = int(input("zero or one?"))
    if x == 1:
        one += 1
    else:
        zero += 1
if one > zero:
    print(one)
elif one == zero:
    print(one)
else:
    print(zero)
