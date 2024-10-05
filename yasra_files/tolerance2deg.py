import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from matplotlib import gridspec

x = []
y1 = []
y2 = []
x1 = []
y11 = []
y12 = []  # for upper axis
x2 = []
y21 = []

f, (ax2, ax) = plt.subplots((2), sharex=True, figsize=(10.1, 5.1))

gs = gridspec.GridSpec(2, 1, height_ratios=[1, 3])
ax = plt.subplot(gs[1])
ax2 = plt.subplot(gs[0])

f.subplots_adjust(left=0.08, right=0.98, top=.97, bottom=.1)
f.subplots_adjust(hspace=0)

for item in ([ax.xaxis.label] +
				 ax.get_xticklabels() + ax.get_yticklabels() + ax2.get_yticklabels()):
	item.set_fontsize(11)

with open('log_temp2deg.txt') as f:
	while True:
		lines = f.readlines(43200)
		if not lines:
			break
		for line in lines:
			p = line.split('	')
			y1.append(float(p[3]))
			y2.append(float(p[4]))

yvals1 = np.array(y1)
yvals2 = np.array(y2)

xvals = np.arange(0, 86400, 2)

with open('heat duplicate 2.txt') as f:
	while True:
		lines = f.readlines(62)
		if not lines:
			break
		for line in lines:
			print
			line
			p = line.split('	')
			x1.append(float(p[0]))
			y11.append(float(p[2]))
			y12.append(float(p[1]))
xvals1 = np.array(x1)
yvals11 = np.array(y11)
yvals12 = np.array(y12)


ax.plot(xvals / 3600, yvals1, 'r', linewidth=1.5, label="Outside temperature")
ax.plot(xvals / 3600, yvals2, 'blue', linewidth=1.5, label="Inside temperature")
# ax.plot(xvals1 / 3600, yvals11, 'green', linewidth=1)

ax2.plot((xvals1*2) / 3600, yvals12, 'green', linewidth=1)

ax.yaxis.set_visible(True)
ax2.xaxis.set_visible(False)

ax.set_ylabel('Temperature[Degree]', fontsize=17, labelpad=1.2)
ax2.set_ylabel('Heater status', fontsize=15, labelpad=0)
ax.set_xlabel('Time[Hour]', fontsize=17, labelpad=0)

labels1 = [item.get_text() for item in ax.get_xticklabels()]
labels1[1] = '9AM'
labels1[2] = '1PM'
labels1[3] = '5PM'
labels1[4] = '9PM'
labels1[5] = '1AM'
labels1[6] = '5AM'
labels1[7] = '9AM'

ax.set_xticklabels(labels1)

labels = [item.get_text() for item in ax2.get_yticklabels()]
labels[1] = 'OFF'
labels[2] = 'ON'
ax2.set_yticklabels(labels)

ax.set_xlim(0, 24)
ax.set_ylim(12, 25)
ax2.set_xlim(0, 24)
ax2.set_ylim(-0.1, 1.1)

ax.xaxis.set_major_locator(ticker.MultipleLocator(4))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(1))

ax.text(5, 15, '2 degree tolerance',
		horizontalalignment='center',
		verticalalignment='center', fontsize="15")

ax.legend(fontsize="14", frameon=False)

plt.show()
