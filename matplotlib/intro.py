# Introduction to Matplotlib
# It is used to convert boring data into beautiful graphs and visualizations.

#RULES:
# 1. Ask the story/question. Don't start with chart directly.
# 2. Choose the right chart type or match the chart according to the data.
# 3. Keep it simple and label everything.
# 4. Use colors wisely and keep it simple and don't overdo it.
# Story -> Chart -> Clarity

#Seaborn uses matplotlib interanally for plotting graphs. It uses less code and also makes the graphs look better by default.
print('Intro to Matplotlib')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

print("Matplotlib imported successfully!")
## MATPLOTLIB BASICS:

print('Matplotlib Basics')
#Anatomy of a matplotlib plot:

#Structure: The entire window or figure that contains all the plot elements.
#Figure: The diagram or chart created using x and y axes which can be modified using various functions.
#Axes: The area where the data is plotted, including the x-axis and y-axis.
#Axis: The individual x-axis or y-axis that defines the scale and range of the data
#Labels: Textual information added to the plot, such as titles, axis labels, and legends.
#Title: The main heading of the plot that describes what the plot represents.
#Legend: A box that explains the symbols, colors, or patterns used in the plot to differentiate between different data types or categories.

#Categorical vs Numerical Columns:
#Categorical: Data that represents distinct categories or groups (e.g., colors, types, labels) basically text.
#Numerical: Data that represents continuous values or measurements (e.g., height, weight, temperature) basically numbers.

#Types of Data:
#Ordinal Data: Categorical data with a specific order or ranking (e.g., small, medium, large). Example: 10th,12th,Btech,Mtech,PhD,PostDoc is an ordinal data as there is a specific order/rank/sequence in these educational degrees. You can not go to PhD before completing 10th.
#Nominal Data: Categorical data without any specific order or ranking (e.g., colors, types of fruits).
#Discrete Data: Numerical data that can only take specific values and we can segregate (e.g., number of students in a class).
#Continuous Data: Numerical data that we can not segregate (e.g., sales values). 
#Time Series Data: Data that is collected over time, often used to analyze trends and patterns (e.g., stock prices over time).
#Quantitative Data: Numerical data that represents quantities or measurements (e.g., age, income, temperature).
#Qualitative Data: Categorical data that represents qualities or characteristics (e.g., colors, types of fruits, customer satisfaction levels).


x_val = [3,6,7]
y_val = [2,5,8]

plt.plot(x_val, y_val) #Plots a line graph with x_val on x-axis and y_val on y-axis
plt.show() #Displays the plot


# How to choose the right plot?
#Univariate vs Bivariate vs Multivariate:
#Univariate Analysis: Analyzing a single variable or feature in a dataset (e.g., histogram of ages). Ex: Like you are given just the age, so you can add conditions like less than 18, between 18-60, greater than 60 and plot a histogram.
#Bivariate Analysis: Analyzing the relationship between two variables or features in a dataset (e.g., scatter plot of height vs weight).
#Multivariate Analysis: Analyzing the relationships among three or more variables or features in a dataset (e.g., pair plot showing relationships among multiple features).


## UNIVARIATE PLOTS:

#Category of Plots:
#Categorical Plots: Bar Plot, Pie Chart, Count Plot
#Numerical Plots: Line Plot, Scatter Plot, Histogram, Box Plot

# BAR GRAPH EXAMPLE:
# X = category.index
# Y = category.values
# plt.figure(figsize=(8, 5)) #Sets the figure size to 8 inches wide and 5 inches tall
# plt.bar(X, Y, width=0.4, color='blue') #Plots a bar graph with categories A,B,C on x-axis and their corresponding values on y-axis
# plt.xticks(rotation=45, fontsize=10) #Rotates the x-axis labels by 45 degrees for better readability
# xticks represents the labels on x-axis
# plt.yticks(fontsize=10) #Sets the font size of y-axis labels to 10
# plt.xlabel('Categories', fontsize=12) #Sets the label for x-axis
# plt.ylabel('Values', fontsize=12) #Sets the label for y-axis
# plt.title('Bar Graph Example', fontsize=14) #Sets the title of the plot
# plt.show() #Displays the plot

# PIE CHART EXAMPLE: Displays proportion of each category (%)
# pyplot doesnot exist in seaborn
# plt.pie(data=[30, 20, 50], labels=['A', 'B', 'C'], colors=['red', 'blue', 'green'], autopct='%1.1f%%', startangle=140, explode=(0.1, 0, 0))

#Statistical Plots: Used to visualize statistical properties of data distributions like mean, median, variance, outliers.
#Examples: Box Plot, Violin Plot, Swarm Plot, Strip Plot, Histogram, Density Plot, Q-Q Plot

# HISTOGRAM EXAMPLE:
plt.hist(x_val, bins=5, color='blue', alpha=0.7) #Plots a histogram of x_val with 5 bins,(bars bydefault is 10)
sns.histplot(x_val, bins=5, color='blue', kde=True) #Seaborn histogram with KDE
plt.xlabel('X Values') #Sets the label for x-axis
plt.ylabel('Frequency') #Sets the label for y-axis
plt.title('Histogram Example') #Sets the title of the plot
plt.show() #Displays the plot
# This helps in understandig skewdness(
#  - left skewed: if the points are concentrated on the right, 
#  - right skewed: if the points are concentrated on the left, also in right, it should be positive always. 
#  - Normal distribution: bell shaped, ideal condition), kurtosis, outliers in the data

#KDE: Kernel Density Estimate
#It is a smoothed version of histogram that estimates the probability density function of a continuous random variable.
#It helps in visualizing the distribution of data points and identifying patterns or trends in the data.

# Mean = Median = Mode only when the data does not have any outliers and is perfectly symmetrical.

#BOX PLOT EXAMPLE: give view of numerical data of statical data in better way and also tells about the noise
# ---------------
# |     o       |     <- Outlier (data point that is significantly different from other data points)
# |     |        |   <- Maximum (Q3 + 1.5*IQR)           [UPPER WHISKER]
# |   -------   |   <- Q3 (75th percentile)
# |   |     |   |
# |   | --- |   |   <- Interquartile Range (IQR = Q3 - Q1) Median (50th percentile)
# |   |     |   |
# |   -------   |   <- Q1 (25th percentile) this point of data will be greater than 25% of the data (below) and less than 75% of the data (above)
# |     |       |                              [LOWER WHISKER]
# |     |       |   <- Minimum (Q1 - 1.5*IQR)
# ---------------       <-  Box Plot            

# plt.boxplot(x_val) #Plots a box plot of x_val


# Chart Type	Best For	                  Example
# Line Chart	Trends over time	          Sales over months
# Bar Graph	    Compare categories	          Revenue by product
# Pie Chart	    Part of a whole	              Market share
# Box Plot	    Data spread & outliers	      Test scores
# Histogram	    Data distribution	          Age or weight data
# Count Plot	Frequency of categories	      Count of users by city

# “Find the range in which most students scored” → Histogram
# If they said
# “Compare score distributions or check outliers” → Box Plot


## BIVARIATE PLOTS:

#Category of Plots:
#Numerical + Categorical Plots: Violin Plot, Swarm Plot, Strip Plot

## [Numerical + Numerical Plots: Heatmap, Pair Plot, Scatter Plot, Line Plot]
# LINE PLOT EXAMPLE: I can represent two numerical variables, like time and sales, using a line plot to show how sales change over time.
# We use it when:
# Continuous data points need to be connected to show trends over time or ordered categories.
# Highlighting/Comparing the overall trend or pattern in the data rather than individual data points.
# To see data over the time, sequential data.
# To visualize changes in data over intervals, such as stock prices, temperature changes, or sales figures over time.
# Example: To find which game was popular over the years, we can use line plot to show the trend of game popularity over time.

# MATPLOTLIB LINE PLOT EXAMPLE:
plt.plot(x_val, y_val, marker='o', linestyle='-', color='blue') #Plots a line graph with markers at each data point
plt.xlabel('X Values') #Sets the label for x-axis
plt.ylabel('Y Values') #Sets the label for y-axis
plt.title('Line Plot Example') #Sets the title of the plot
plt.xlim(0, 10) #Sets the x-axis limits from 0 to 10
plt.xlim(left=0, right=10) #Another way to set x-axis limits from 0 to 10
plt.show() #Displays the plot

# SEABORN LINE PLOT EXAMPLE:
sns.lineplot(x=x_val, y=y_val, marker='o', color='green', label='Line 1') # Can plot multiple lines in the same graph by adding another sns.lineplot() with different data
sns.lineplot(x=y_val, y=x_val, marker='o', color='red', label='Line 2')
plt.legend(loc='upper left') #Adds a legend to the plot at the specified location
plt.xlabel('X Values') #Sets the label for x-axis
plt.ylabel('Y Values') #Sets the label for y-axis
plt.title('Seaborn Line Plot Example') #Sets the title of the plot
plt.show() #Displays the plot - graph above this cmnd is freezed and for new changes you need to write above it

# SCATTER PLOT EXAMPLE:
# These are bubbles which don't connect with each other
# If there's too much data points, line plot may not help us distinguish between them, so we use scatter plot to see the distribution of data points.
# Example: Age of car vs Resale value of car, line plot won't help here as there are multiple cars with same age but different resale value, so scatter plot will help in visualizing the distribution of data points.
# In short we can say, if x has multiple y values for same x, we use scatter plot.

# MATPLOTLIB SCATTER PLOT EXAMPLE:
plt.scatter(x_val, y_val, color='blue', marker='o') #Plots a scatter plot with x_val on x-axis and y_val on y-axis
plt.xlabel('X Values') #Sets the label for x-axis
plt.ylabel('Y Values') #Sets the label for y-axis
plt.title('Scatter Plot Example') #Sets the title of the plot
plt.show() #Displays the plot

# SEABORN SCATTER PLOT EXAMPLE:
sns.scatterplot(x=x_val, y=y_val, color='green', marker='o') #Seaborn scatter plot
plt.xlabel('X Values') #Sets the label for x-axis
plt.ylabel('Y Values') #Sets the label for y-axis
plt.title('Seaborn Scatter Plot Example') #Sets the title of the plot
plt.show() #Displays the plot

#Correation: It means if one feature increases, the other feature also increases (positive correlation) or decreases (negative correlation).
# If one feature affects the other feature it has high correlation but if it doesnot affect the other feature it has low correlation.
# If one feature affects the other feature directly is called causation, but correlation doesnot imply causation.
# Correlation Coefficient: A numerical value between -1 and 1 that indicates the strength and direction of the linear relationship between two variables.
# +1 indicates a perfect positive correlation, -1 indicates a perfect negative correlation, and 0 indicates no correlation.
# We use heatmaps to visualize correlation matrices, which show the correlation coefficients between multiple variables in a dataset.

# HEATMAPS: They are grid like strcutural representation.
# Here, we want to understand the quantitative analysis between input and output data



## [Categorical + Categorical Plots: Clustered Bar Plot, Stacked Bar Plot, Dodged Bar Plot]
# Because both are text data, we need to use aggregation functions to summarize the data before plotting.
# For example, we can use count or mean to aggregate the data.

# STACKED BAR PLOT EXAMPLE: Want to check the ratio of each category with total
# In a stacked bar plot, we stack the bars on top of each other to show the total value and the contribution of each category.
# This is useful when we want to compare the total values across categories and also see the breakdown of each category.

# DODGED BAR PLOT EXAMPLE: compare in same/diff categories
# In a dodged bar plot, we place the bars next to each other instead of stacking them.
# This is useful when we want to compare the values of different categories side by side.

# EXAMPLE: How can we compare the top three publishers?

categories = ['A', 'B', 'C']
men = [20, 34, 30]
women = [25, 32, 34]

# MATPLOTLIB:
# STACKED
plt.bar(categories, men, label='Men')
plt.bar(categories, women, bottom=men, label='Women')  # stack on top
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Stacked Bar Plot')
plt.legend()
plt.show()

#DODGED
x = np.arange(len(categories))  # positions for bars
width = 0.35  # bar width

plt.bar(x - width/2, men, width, label='Men')
plt.bar(x + width/2, women, width, label='Women')

plt.xticks(x, categories)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Dodged (Grouped) Bar Plot')
plt.legend()
plt.show()

# SEABORN:
#DODGED
df = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Gender': ['Men', 'Women'] * 3,
    'Value': [20, 25, 34, 32, 30, 34]
})

sns.barplot(x='Category', y='Value', hue='Gender', data=df)
plt.title('Dodged (Grouped) Bar Plot')
plt.show()

# Seaborn doesn’t have stacked bars by default,
# but you can achieve it by using Pandas + Matplotlib:
# STACKED
df_pivot = df.pivot_table(index='Category', columns='Gender', values='Value')
df_pivot.plot(kind='bar', stacked=True)
plt.title('Stacked Bar Plot (using Seaborn Data)')
plt.show()

#pd.crosstab() expects actual data (Series or arrays) — not just column names as strings.
stacked = pd.crosstab(index=df['Category'], columns=df['Gender'], values=df['Value'], aggfunc='sum')
stacked.plot(kind='bar', stacked=True)
plt.show()

# Matplotlib → Stacked
# Seaborn → Dodged

# You can use boxplot to know about the outliers and the comparisons btw categories
