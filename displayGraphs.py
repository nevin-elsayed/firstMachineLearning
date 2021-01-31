from imports import *

# Visualizing the Data

# Load dataset
data = "iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(data, names=names)

# Univariate plots help better describe each attriubute

# Box and Whisker Plot
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

# Histogram 
dataset.show()
pyplot.show()


# Multivarite plots help better show interactions of variables

# Scatter Plot Matrix 
scatter_matric(dataset)
pyplot.show()