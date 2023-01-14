t0 = 0
tF = 4
y0 = 1
h = 0.25

def yact(t):
    return(pow(2/3 * pow(t,3) + 1, (1/2)))

t = t0
y = y0
yactual = yact(t0)

print('step', '\t''t', '\t''\t''y approx', '\t''\t''y actual')
print(0, '\t'''"%.8f" % t, '\t'''"%.8f" % y, '\t'"%.8f" % yactual)
n = 0

def fe(t, y, h):
    def f(t, y):
        return ((1/y) * pow(t,2))
    return(y + h * f(t, y))

def me(t, y, h):
    def f(t, y):
        return ((1/y) * pow(t,2))
    return(y + h * f((t + h/2), (y + (h/2) * f(t, y))))

def te(t, y, h):
    def f(t, y):
        return ((1/y) * pow(t,2))
    return (y + (h/2) * (f(t, y) + f((t + h), (y + h * f(t, y)))))

#while (t+h <= tF):
while (n <= 8):
    t = t + h
    n = n + 1
    y = fe(t, y, h)
    yactual = yact(t)
    # y = me (t, y, h)
    # y = te(t, y, h)
    print(n, '\t'''"%.8f" % t, '\t'"%.8f" % y, '\t'"%.8f" % yactual)

