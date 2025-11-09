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
hours = float(input('how many hours did you study: '))
prediction = model.predict([[hours]])
 # have to pass in 2d array as the data is a table where row is considered to be example and col as a feature
# if you pass in just [value] it won't know for which feature we are talking about

print(f'you will score around: { prediction }')

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
hours = float(input('how many hours did you study: '))
prediction = model.predict([[hours]])

if(prediction): print('PASS')
else: print('FAIL')

'''
### KNN:
-------------------------
'''