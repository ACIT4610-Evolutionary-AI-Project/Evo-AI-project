from pylab import *

import matplotlib.pyplot as plt

plt.style.use('seaborn')

x = [8, 9, 7, 9]
y = [3, 2, 4, 8]
colors = [7, 5, 2, 7]
plt.scatter(x, y, s=200, c=colors, edgecolors='black', cmap='Greens', linewidths=1, alpha=0.75)
cbar = plt.colorbar()
cbar.set_label('Infection')
grades_range = [10, 20, 30, 40]
fig = plt.figure()
# ax = fig.add_axes([0, 0, 1, 1])
# ax.scatter(grades_range, x, color='r')
# ax.scatter(grades_range, y, color='b')
# plt.xlabel('Grades Range')
# plt.ylabel('Grades Scored')
# plt.title('scatter plot')
# plt.tight_layout()
plt.show()
