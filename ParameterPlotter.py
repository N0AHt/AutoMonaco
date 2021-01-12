import matplotlib.pyplot as plt

data = [[10, 0.035],

[20, 0.228],

[30, 0.733],

[40, 1.503],

[50, 2.381],

[60, 3.25],

[70, 4],

[80, 4.61],

[90, 5.01],

[100, 5.25]]

xvals = [i[0] for i in data]
yvals = [i[1] for i in data]

plt.plot(xvals, yvals)
plt.xlabel('RL value (%)')
plt.ylabel('Recorded Output Power (w)')
plt.show()
