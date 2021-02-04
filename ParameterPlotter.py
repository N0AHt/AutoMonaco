import matplotlib.pyplot as plt
import numpy as np

data = [[5, 0.006],

[10, 0.034],

[15, 0.100],

[20, 0.229],

[25, 0.440],

[30, 0.735],

[35, 1.098],

[40, 1.507],

[45, 1.946],

[50, 2.392],

[60, 3.25],

[65, 3.64],

[70, 4.01],

[75, 4.33],

[80, 4.6],

[85, 4.83],

[90, 5.00],

[95, 5.14],

[100, 5.24]]

xvals = [i[0] for i in data]
yvals = [i[1] for i in data]

degree = 10
poly = np.polyfit(xvals, yvals, degree)
x_vals1 = np.arange(100)
function = np.polyval(poly, x_vals1)
# xlist = [i for i in range(0,100)]
# ylist = [function(float(xlist[i]) for i in xlist)]

# plt.figure(1)
# plt.plot(xvals, yvals)
# plt.xlabel('RL value (%)')
# plt.ylabel('interpolated Recorded Output Power (w)')
# plt.title(poly)
# plt.show(1)


plt.plot(x_vals1, function)
plt.plot(xvals, yvals)
plt.title('overlaid power graph')
plt.show()
