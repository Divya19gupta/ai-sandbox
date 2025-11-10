'''
### INTRODUCTION TO ML (1)
-------------------------
1) Regression - It predicts numbers.

Types:
------ 
    a) Linear Regression: Predicts the next number to form a straight line
    b) Classification: Predicts a category/label (Yes/No)
    Types:
    ------
        i) Logistic Regression: Classifies a category based on 0/1
        ii) KNN: It takes decision based on the data points around it
        iii) Decision Tree Clasifier: Works on the basis of flowchart.

2) Model Training: 
    - fit(): Train your model based on your data
    - predict(): Use the train model to give predictions
'''

'''
### LINEAR REGRESSION:
-------------------
1) Learns the pattern of the model
2) Creates a straight line
3) Predicts the next point using that st line
=> Formula: y = mx + b
'''

from sklearn.linear_model import LinearRegression
model = LinearRegression() #creating an object
X = [[1],[2],[3],[4],[5]]
y = [34,66,7,88,100]
model.fit(X,y)
# hours = float(input('how many hours did you study: '))
# prediction = model.predict([[hours]])
 # have to pass in 2d array as the data is a table where row is considered to be example and col as a feature
# if you pass in just [value] it won't know for which feature we are talking about

# print(f'you will score around: { prediction }')

'''
### LOGISTIC REGRESSION:
-------------------------
1) Classifies on the basis of labels
'''

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
X = [[1],[2],[3],[4],[5]]
y = [0,0,1,1,1]
model.fit(X,y)
# hours = float(input('how many hours did you study: '))
# prediction = model.predict([[hours]])

# if(prediction): print('PASS')
# else: print('FAIL')

'''
### KNN:
-------------------------
1) works slow with big data as it checks neighbours
2) choose odd values of k
'''

from sklearn.neighbors import KNeighborsClassifier
X = [
    [120,3],
    [150,5],
    [200,7],
    [250,9],
    [300,10]
]
Y = [0,0,1,1,1]
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X,y)
# weight = float(input('Enter weight of the fruit'))
# qnt = float(input('Enter quantity of the fruit'))
# prediction = model.predict([[weight,qnt]])[0] #we are using zero as it returns a list of predictions, but if we want one value we need to add 0 
# if prediction: print('orange')
# else: print('apple')

'''
### Decision Tree:
-------------------------
'''
from sklearn.tree import DecisionTreeClassifier

X = [
    [3,2],
    [5,4],
    [7,8],
    [9,9]
]
y = [0,0,1,1] 
model = DecisionTreeClassifier()
model.fit(X,y)
size = float(input('Enter size: '))
color = float(input('Enter color (1-10): '))
prediction = model.predict([[size,color]])[0]
if prediction: print('orange')
else: print('apple')

# .fit() is a method to understand the pattern through input and output (X,y). It is done only once in the code.
# .predict() is a method in which we feed in a new data and model gives the answer according to how training is done
# overfitting happens when the model learns too much about the data during training and it fails when new details are given.
# underfitting happens when the model is not trained properly enough to recognise the data.
# goodfit happens when the model understands the reference data and is able to generalise a prediction. 
