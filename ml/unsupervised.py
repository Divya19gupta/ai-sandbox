'''
CLUSTERING:

1) KMeans Clustering: It creates clusters (groups datapoints) according to patterns observed
5 Step Process:
    - Tell the machine how many groups you need to create
    - drop any 3 random points (which are called centroid) which are starting points
    - rest of the data points will join the similar group leaders (above 3 points)
    - then you try to find the center of the grop such that you move the leader to the center forming better shaped clusters
    - conitnue this process till it's settled

2) Elbow Method: 
- In the graph of inertia (how spread out is the data) vs no of clusters
- When K=1, the value of inertia is very high, meaning that all the data points are spread out too much forming just one group
- And as the value of K increases, inertia decreases, and the value of K is best when we achieve the elbow curve 

3) PCA: When you don't need all the columns to analyse the data but only a few(summarised) of them without losing the information

It is need because:
    - Overfitting
    - How will you visualise/understand such a big data?
    - Model becomes slower on such a large dataset

We use standard scaling here to reduce the data in similar range because

'''