# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
import matplotlib.pyplot as plt
import numpy as np
import os


plt.figure(figsize = (8,6), dpi = 80)
plt.subplot(1,1,1)

x = np.linspace(-np.pi, np.pi, 256, endpoint = True)
c, s = np.cos(x), np.sin(x)

plt.plot(x,c,'b-', linewidth = 1, label = 'cosine')
plt.plot(x,s, 'r-', linewidth = 1, label = 'sine')
plt.legend(loc = 'upper left')

plt.xlim(-4.0,4.0)
plt.ylim(-1.0,1.0)

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.yticks([-1, 0, +1],
          [r'$-1$', r'$0$', r'$+1$'])

ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2, linestyle="--")
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')

plt.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t, t],[0, np.sin(t)], color='red', linewidth=2, linestyle="--")
plt.scatter([t, ],[np.sin(t), ], 50, color='red')

plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

print('Plot created')
my_path = 'C:/Users/dgaviria6/.spyder-py3/my_saved_images' 
inp = input('Save as: ')
my_file = inp+ '.png'

plt.savefig(os.path.join(my_path, my_file), dpi=72)
print('Saved as {} in {}' .format(my_file, my_path))

plt.show()
