'''
## MEAN & CENTROID:
----------------------
1) Mean: It is average divide by total
2) Centroid: On the graph the center point considering both axis (xmid,ymid). This is what KMeans try to find. 
It tried to find the middle in each group to get an idea how to divide the clusters in categories

- So if you ask the machine who's my regular customer it'll use centroid and then use mean to compare if the value is more or less
for clustering the similar type of data togeather using centroid

Centroid = Mean point in many dimensions
Mean = Average value in one dimension

## EUCLIDEAN DISTANCE:
-------------------------
Helps in finding distance between two data points which in turns tells if they are similar (closer) to each other or different.

FOARMULA: distance = sqrt((x-x')^2 + (y-y')^2)

USED IN ML:
    - KNN: Closest group to assign a new data point
    - KMeans Cluster: decides the closeness to the group
    - Outliers: Helps in identifying fraud data points

## VARIANCE AND SPREAD:
--------------------------
So, if the data is too different from each other (like someone is scoring 10 marks and the other person is getting 90) we call it spread, mathematically varience.
PCA(Priciple component analysis) works on using this principle to compress a large data into a less readable row by not losing any information.
It uses high varience to analyse which is important data to keep and which similar datas can be merged. Also, helps in understanding which features to keep and which one to drop

FORMULA: ((x1.x')^2 + ... + (xn.x')^2) / n

x1 = data points
x' = mean 
n = total points

## LINEAR ALGEBRA:
--------------------
Tells about data kaha zayada change hora hai
'''