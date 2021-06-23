import matplotlib.pyplot as plt
import numpy as np

data = [[1000, 4.66],
[500, 2.305],
[333.33, 1.537],
[250, 1.151],
[200, 0.919],
[166.66, 0.765],
[142.85, 0.655],
[125, 0.573],
[111.11, 0.508
]]


xvals = [i[0] for i in data]
yvals = [i[1] for i in data]

plt.figure(1)
plt.plot(xvals, yvals)
plt.xlabel('Output Frequency (kHz)')
plt.ylabel('Recorded Output Power (w)')
plt.title('Power vs Output Frequency')
plt.show(1)
