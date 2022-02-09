# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 09:49:14 2018

@author: dgaviria6
"""

#%%

import matplotlib.pyplot as plt

data = {0:3, 6:3, 4:2}
xValues = list(data.keys())
yValues = list(data.values())


plt.plot(xValues, yValues, 'ro-', linewidth=2, markersize=12)
plt.show()
    
#%%
import matplotlib.pyplot as plt

plt.plot(data)
plt.ylabel('some numbers')
plt.show()
#%%
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])


plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1, 2, 3') # subplot 211 title
#%%
import numpy as np
a = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
print(a)

p = np.poly1d([1,6,5])
print(p.roots)
#%%
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 20)
y = np.cos(x) + 0.3*np.random.rand(20)
p = np.poly1d(np.polyfit(x, y, 3))

t = np.linspace(0, 1, 200)
plt.plot(x, y, 'o', t, p(t), '-')   
#%%
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 2000)
y = np.cos(x) + 0.3*np.random.rand(2000)
p = np.polynomial.Chebyshev.fit(x, y, 90)

t = np.linspace(-1, 1, 200)
plt.plot(x, y, 'r.')   

plt.plot(t, p(t), 'k-', lw=3)   
#%%
import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('C:/Users/dgaviria6/.spyder-py3/my_text_files/populations.txt')
new_data = data[5:,:3]
print('   Year  Hare   Lynx')
print(new_data)


