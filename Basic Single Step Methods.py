import math
t0 = 0
tF = 2
y0 = 5
h = 0.25

def yact(t):
    return((5 * pow(math.e,t)) / (5 * pow(math.e,t) - 4))

t = t0
y = y0
yactual = yact(t0)

print('k', '\t''t', '\t''\t''\t''y_k', '\t''\t''\t''y(t_k)')
print(0, '\t'''"%.8f" % t, '\t'''"%.8f" % y, '\t'"%.8f" % yactual)
n = 1

def fe(t, y, h):
    def f(t, y):
        return (y*(1-y))
    return(y + h * f(t, y))

def me(t, y, h):
    def f(t, y):
        return (y*(1-y))
    return(y + h * f((t + h/2), y + (h/2) * f(t, y)))

def te(t, y, h):
    def f(t, y):
        return (y*(1-y))
    return (y + (h/2) * (f(t, y) + f((t + h), (y + h * f(t, y)))))

while (t+h <= tF):
#while (n <= 8):
    # y = fe(t, y, h)
    # y = me (t, y, h)
    y = te(t, y, h)
    yactual = yact(t + h)
    print(n, '\t'''"%.8f" % t, '\t'"%.8f" % y, '\t'"%.8f" % yactual)
    t = t + h
    n = n + 1

