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

# We use standard scaling here to reduce the data in similar range (called z-scores) because to avoid biases on large data
# FORMULA: z-scores = (x - mean)/ std deviation, where x = original value
You get z-scores per column, and also 
    - 0 means avg value
    - -ve means below avg
    - +ve means above avg
    - Center of PCA (0,0)
the scaling (z-scoring) is done per column (feature), not per value or across all values combined.

# We also use Decomposition breaks high dimesional data into small parts
# Further fit_transform() method is used, where they need to learn the mean/std deviation of the data given and transform means to apply that logic to scale the data

EXAMPLE:
So there's a data of a candidate with 4 features like resume, projects, extra curricular and education
now what PCA will do is compress the above 4 features into two let's say like career readiness (holding 95% of the data) and soft skills (holding like 0.5% of the data)
Now the final HR will look only final two features instead of going through such a big dataset of 4 features mentioned initially

'''