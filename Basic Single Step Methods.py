import math

t0 = 0
tF = 4
y0 = 5
h = 0.125

t = t0
y = y0
print("%.8f" % t, "%.8f" % y)

while (t+h <= tF):
    y = fe(t, y, h)
    # y = me (t, y, h)
    # y = te(t, y, h)
    t = t + h
    print("%.8f" % t, "%.8f" % y)







