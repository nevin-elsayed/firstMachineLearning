from imports import *
# Cut dataset in into pieces
array = dataset.values

X = array[:,0:4]
y = array[:,4]

# Training 80% of the data, remaining 20% is left for reference
X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size = 0.20, random_state = 1)

# Building Models with 6 differnt algorithms
models = []

# Simple Linear Algorithms 
# Logistic Regression (LR)
models.append(('LR', LogisticRegression(solver = 'liblinear', multi_class="ovr")))

# Linear Discriminant Analysis (LDA)
models.append(('LDA', LinearDiscriminantAnalysis()))

# Non-Linear Algorithms
# K-Nearest Neighbors (KNN)
models.append(('KNN', KNeighborsClassifier()))

# Classification and Regression Trees (CART)
models.append(('CART', DecisionTreeClassifier()))

# Gaussian Naive Bayes (NB)
models.append(('NB', GaussianNB()))

# Support Vector Machines (SVM)
models.append(('SVM', SVC(gamma = 'auto')))

# Evaluate Models
results = []
names = []

for name, model in models:
# Using k-fold cross validation with k = 10
    kfold = StratifiedKFold(n_splits = 10, random_state = 1, shuffle =  True)
    cv_results =  cross_val_score(model, X_train, y_train, cv = kfold, scoring = 'accuracy')
    results.append(cv_results)
    names.append(name)
    print('%s; %f (%f)' % (name, cv_results.mean(), cv_results.std()))


# Display Algorithm Performance with a historgram

pyplot.boxplot(results, labels = names)
pyplot.title('Algorithm Comparison')
pyplot.show()
