import math

#Defining variables
tzero = 0
tF = math.pi
hmin = 1 / pow(2, 11)
yzero = 1
lamb = (-1) * 30

#Defining functions
def f(t,y):
    return(lam * (y - math.cos(t)) - math.sin(t))

#Initialization
t = tzero
y = yzero
emaxold = 0
h = 0.25

print('h', '\t''\t''\t''max error', '\t''\t''\t''error ratio')

#First while loop for h values
while (h >= hmin):
    print(h)
    emax = 0
    tmax = 0
    t = tzero
    y = yzero

    while ((t + h) <= tF):
        print(t)
        # y = fe(t, y, h)
        # y = bee(t, y, h)
        # y = m(t, y, h)
        # y = te(t, y, h)
        # y = tpc(t, y, h)
        t = t + h
        # actual = yact(t)
        # e = abs(y - actual)






