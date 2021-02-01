from imports import *
# Cut dataset in into pieces
array = dataset.values

X = array[:,0:4]
y = array[:,4]

# Training 80% of the data, remaining 20% is left for reference
X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size = 0.20, random_state = 1)

# Develop predictions on data
model = SVC(gamma = 'auto')
model.fit(X_train, y_train)
predictions = model.predict(X_validation)


# Evaluate predictions
print(accuracy_score(y_validation, predictions))
print(confusion_matrix(y_validation, predictions))
print(classification_report(y_validation, predictions))