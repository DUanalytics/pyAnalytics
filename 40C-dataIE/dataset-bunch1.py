# Create a bunch type of data objects
import numpy as np
import sklearn.datasets
examples = []
examples.append('A')
examples.append('B')
examples.append('C')
examples.append('D')

target = np.zeros((4,), dtype=np.int64)
target[0] = 1
target[1] = 0
target[2] = 1
target[3] = 0
examples
target

dataset = sklearn.datasets.base.Bunch(data=examples, target=target)
dataset
type(dataset)
