import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

youtube_data = pd.read_csv('video_result.csv')
# Diplays the correlation between each column in the csv
print(youtube_data.corr())

plt.figure()
hist, edge= np.histogram(youtube_data.viewCount)
plt.bar(edge[:-1], hist, width = 1)
