import matplotlib.pyplot as plt

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

plt.plot(xvals, yvals)
plt.xlabel('RL value (%)')
plt.ylabel('Recorded Output Power (w)')
plt.show()
