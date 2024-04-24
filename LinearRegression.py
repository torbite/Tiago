
coef = (1087-723)/(4 - 0)
y_0 = 723
def y(x):
    return (coef * (x - 2010) + y_0)
a = input("ano? ")
x = int(a)
print(y(x))

