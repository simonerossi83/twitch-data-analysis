import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

plt.figure(figsize=(10,8))
plt.bar(range(len(games)),viewers)
ax = plt.subplot()
plt.title('Most viewed games - 2015')
plt.xlabel('Games')
plt.ylabel('Number of users')
ax.set_xticks(range(len(games)))
ax.set_xticklabels(games)
plt.show()

# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']

plt.figure(figsize=(10,8))
#plt.clf()
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
plt.pie(countries, explode=explode, colors=colors, shadow=True, startangle=345, autopct='%1.0f%%', pctdistance=1.15)
plt.title("League of Legends Viewers' Whereabouts")
plt.legend(labels, loc="right")
#plt.axis('equal')
plt.show()

# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

plt.figure(figsize=(10,8))
plt.plot(hour, viewers_hour)
plt.xlabel('Hours')
plt.ylabel('Viewers')
plt.title('Number of viewers')
ax = plt.subplot()
ax.set_xticks(hour)
ax.set_xticklabels(hour)
plt.fill_between(hour, [x*.85 for x in viewers_hour], [x*1.15 for x in viewers_hour], alpha=.2)
plt.show()
plt.show()
