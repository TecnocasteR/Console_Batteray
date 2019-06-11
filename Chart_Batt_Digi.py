import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('batterylog_28052019.blx', header=None, sep='\s+')
df.head()

x = df[6]
y = df[7]
z = df[3]-1

fig = plt.figure(figsize=(12,3))
ax = fig.subplots()
ax.plot(x,'ro', label = 'A')
ax.plot(y,'bo', label = 'B')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Volt')
ax.set_title('Status')
##grid(color='r', linestyle='-', linewidth=2)
plt.grid(True)
ax.set_xticks((z))
ax.set_xticklabels((z+1))
ax.legend()
plt.axis([0, 43, 0, 8])
plt.show()





