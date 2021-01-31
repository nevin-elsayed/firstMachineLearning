from imports import *

# Check the versions of libraries

print('\nVerifying installations of current libraries below: \n')

# Python version
print('Python: {}'.format(sys.version))
# scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
print('sklearn: {}'.format(sklearn.__version__))

# Shape: should return (150, 0)
print("\nDataset Shape:")
print(dataset.shape)

# Head: should return the first 20 tuples
print("\nDataset Head:")
print(dataset.head(20))


# Summary
print("\nDataset Summary:")
print(dataset.describe())

# Grouping: Here the parameter is "class"
print("\nDisplaying how many tuples of group type")
print("\nGrouped By:")
print(dataset.groupby('class').size())

