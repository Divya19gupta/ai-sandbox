## METRICS:

# Accuracy: Kitna sahi machine ne prediction krri
# Precision: Jo prediction krri, usmei acutal mei kitni baar sahi thi
# Recall: Jo sahi cheezein thi, vo kitni baar sahi predict krri
# F1-Score: Balance between precision and recall
# R^2: It basically tells how your model is prediction is
#   - less than 0.0: Perfomance worse
#   - 0.0 means that it is just giving the avg prediction w/o considering other real world scenarios
#   - more than 0.0 means the prediction is good, model is learning able to predict well even with new features

## CONFUSION MATRIX:

# TP: Pass hona tha, pass hogya
# TN: Fail hona tha, fail hogya
# FP: Glt pred machine ne pass bola, but fail tha
# FN: Glt pred machine ne fail bola, but pass tha

## 
# MAE: (Mean Absolute Error)
#   - Take the mistake difference
#   - Remove minus
#   - Add all the values
#   - Divide with total number of students

# MSE: (Mean Squared Error) - We do this so that the values with minute difference like 20 and 25, they can be multiplied to understand the difference in the mistake
# Helps in identifying big mistakes in outlier

#    - Take the mistake difference 
#   - Multiply with itself (difference of 5, mul by 5)
#   - Add all of the above
#   - Divide with total students

# RMSE: (Root Mean Squared Error) - To understand the error in real units. Gives answer in human readable form
# Your target variable (actual data) was in grams, RMSE also comes out in grams
# So you can interpret it directly

#   - sqrt(MSE)

