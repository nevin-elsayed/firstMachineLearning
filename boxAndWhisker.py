from imports import *
# Visualizing the Data
# Univariate plots help better describe each attriubute

# Box and Whisker Plot
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()