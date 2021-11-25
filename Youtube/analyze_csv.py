import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

youtube_data = pd.read_csv('video_result.csv')
# Diplays the correlation between each column in the csv
print(youtube_data.corr())

plt.figure()
hist, edge= np.histogram(youtube_data.viewCount)
plt.bar(edge[:-1], hist, width = 1)

# Doing a regression analysis to plot the relation between viewcound and likecount
y = youtube_data.likeCount
x = youtube_data.viewCount
x = sm.add_constant(x)

model = sm.OLS(y,x).fit() # finds the best line of fit.
print(model.summary())