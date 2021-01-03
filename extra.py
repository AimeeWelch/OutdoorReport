#library
import matplotlib.pyplot as plt

#keeps the labels from being cut off when the graph is displayed
plt.rcParams.update({'figure.autolayout': True})
fig, ax = plt.subplots()

# Example data
data = {'UV': 8, 'Ragweed': 2, 'Grass': 2, 'Tree': 0, 'Mold': 4, 'Dust': 4}
levels = list(data.values())
attributes = list(data.keys())
colors = ['#66ff66', '#ffff66', '#ff8c66', '#ff6666']

ax.barh(attributes, levels, align = 'center', color = colors)
ax.set_xlabel('Levels')
ax.set_title('Outdoor Report')
ax.invert_yaxis()

#show graphic
plt.show()