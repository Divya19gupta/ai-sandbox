import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.model_selection import train_test_split

## DATA PROCESSING FUNNEL

# 1. Handling Missing Data: Refer Pandas

# 2. Encoding Categorical Data: Models can't understand text so replace them with values 0/1. But what if there are more than two values?
# So for that, use one-hot encoding converting the entire data into vectors of numbers that model can understand

# 3. Feature Scaling: So if the data set has some column with very high values model might think that it is an important 
# dataset so to avoid that scale the data to similar scale.
# Types:
#     - Standard Scaler: 

data = {
    'StudyHours':[1,2,3,4,5],
    'TestScores':[40,66,11,99,100]
}

df = pd.DataFrame(data)

scaled = StandardScaler()
scaler = scaled.fit_transform(df)

print(pd.DataFrame(scaler,columns=['StudyHours','TestScores'])) # values will be centered around 0

# Formula for Standard Scaler, z = (X - mu)/ noll 
# X = Value
# mu = mean
# noll = std deviation

#     - MinAndMax Scaler:

minmaxscaler = MinMaxScaler()
minmaxscaled = minmaxscaler.fit_transform(df) # learn from all the min and max values of the col and then will rescale btw 0 and 1
print(pd.DataFrame(minmaxscaled,columns=['StudyHours','TestScores']))

# Formula for Minmaxscaler, z = (X - Xmin)/(Xmax - Xmin)

# 4. Splitting of data:

X = df[['StudyHours']]
y = df[['TestScores']]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42) # testsize means that we will test on 20% data and random state means that we have get the same value when trained
print('Training data', X_train)
print('Test data', X_test)

# You are giving the model x_train data and then test it on x_test data and compare it with y_test to check how accurate it is