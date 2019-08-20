#Topic: Blank Linear Regression
#-----------------------------
# Import necessary modules
____
____
____

# Create training and test sets
X_train, X_test, y_train, y_test = ____(____, ____, test_size = ____, random_state=____)

# Create the regressor: reg_all
reg_all = ____

# Fit the regressor to the training data
____

# Predict on the test data: y_pred
y_pred = ____

# Compute and print R^2 and RMSE
print("R^2: {}".format(reg_all.score(X_test, y_test)))
rmse = np.sqrt(____)
print("Root Mean Squared Error: {}".format(rmse))

#https://campus.datacamp.com/courses/supervised-learning-with-scikit-learn/regression-2?ex=7