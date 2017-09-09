"""
Charting and plotting the condensed data helps to better understand and make insightful discoveries.

Data visualization
-----------------
Numerical analysis does not sometimes lend itself to easy understanding.
Indeed, a single image is worth 1,000 words & in this section, it would be worth 1,000 tables comprised of numbers only.
Images present a quick way to analyze data. Differences in size and lengths are quick markers in an image upon which
conclusions can be drawn. There's different ways to represent data (e.g. graphs).

Multiple bar charts
-------------------
In trying to visualize data, stacking a number of bars enables one to further understand how one piece of data or
variable varies with another.

Box plot
---------
The box plot is used to visualize the median value and low and high ranges of a distribution (aka a box & whisker plot).
- useful to easily identify the outliers in a dataset as well as determining in which direction a dataset may be skewed.
The features of the box plot include a box spanning the interquartile range, which measures the dispersion; the outer
fringes of the data are denoted by the whiskers attached to the central box; the red line represents the median.

Pie chart
---------
The pie chart interprets and visually presents data as if to fit into a circle. The individual data points are expressed
as sectors of a circle that add up to 360 degrees. This chart is good for displaying categorical data and summaries too.

Bubble chart
------------
Another variant of the scatter plot is the bubble chart. In a scatter plot, we only plot the x, y points of the data.
Bubble charts add another dimension by illustrating the size of the points. This third dimension may represent sizes of
markets or even profits.
"""

import matplotlib.pyplot as plt
import numpy as np

# Bar chart
# the bars in the graph represent the magnitude along the y-axis:
# data1 = [25., 5., 150., 100.]
# x_values will determine the points on the x-axis where the bars will be drawn.
# 1st bar with data 25 will be drawn on the x-axis where x is 0; 2nd bar with data 5 -> on the x-axis where x is 1, etc.
# x_values = range(len(data1))
# plt.bar(x_values, data1)
# plt.show()

# Multiple bar
# data2 = [[8., 57., 22., 10.], [16., 7., 32., 40.],]
# generates the array with values [0, 1, 2, 3]
# x_values = np.arange(4)
# the first set of bars are drawn first at position x_values + 0.30.
# Thus, the first x values will be plotted at 0.00, 1.00, 2.00 and 3.00.
# plt.bar(x_values + 0.00, data2[0], color='r', width=0.30)
# he second batch of x_values will be plotted at 0.30, 1.30, 2.30 and 3.30:
# plt.bar(x_values + 0.30, data2[1], color='y', width=0.30)

# When the bars are plotted, 8 and 16 will occupy the same x position, side by side.
# plt.show()


# Box plot
# data3 = np.random.randn(50)
# plt.boxplot(data3)
# plt.show()

# Pie chart
# data4 = [500, 200, 50]
# labels = ["Agriculture", "Aide", "News"]
#
# plt.pie(data4, labels=labels, autopct="%1.1f%%")
# plt.show()

# Bubble chart
# with n specify the number of randomly generated x and y values
n = 10
x = np.random.rand(n)
y = np.random.rand(n)
colors = np.random.rand(n)
# Random bubble sizes
area = np.pi *(60 * np.random.rand(n)) ** 2

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

