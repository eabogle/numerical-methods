import math

def yact(t):
    return(math.cos(t))

def fe(t, y, h):
    def f(t, y):
        return (lamb * (y - math.cos(t)) - math.sin(t))
    return(y + h * f(t, y))

def bee(t, y, h):
    def f(t, y):
        return (lamb * (y - math.cos(t)) - math.sin(t))
    return(y + h * f(t + h, y + h * f(t,y)))

def m(t, y, h):
    def f(t, y):
        return (lamb * (y - math.cos(t)) - math.sin(t))
    return(y + h * f((t + h/2), y + (h/2) * f(t, y)))

def tpc(t, y, h):
    def f(t, y):
        return (lamb * (y - math.cos(t)) - math.sin(t))
    return (y + (h/2) * (f(t, y) + f((t + h), (y + h * f(t, y)))))

t0 = 0
tF = math.pi
hmin = 1 / pow(2, -11)
y0 = 1
lamb = (-1) * 30

emaxold = 0.0
h = 0.25

print('h', '\t''\t''\t''max error', '\t''\t''\t''error ratio')

while (h >= hmin):
    print('test1')
    emaximum = 0
    tmax = 0
    t = t0
    y = y0

    while (t + h <= tF):
        print('test2')
        y = fe(t, y, h)
        # y = bee(t, y, h)
        # y = m(t, y, h)
        # y = tpc(t, y, h)
        t = t + h
        actual = yact(t)
        e = abs(y - actual)

        if (e > emaximum):
            emaximum = e

    ratio = emaxold / emaximum
    print(h, '\t'''"%.8f" % emaximum, '\t'''"%.8f" % ratio)
    h = h * (0.5)
    emaxold = emaximum
