#Topic: Visualisation - DT -iris
#-----------------------------
#libraries
#Links : https://pypi.org/project/dtreeplt/
# You should prepare trained model,feature_names, target_names.
# in this example, use iris datasets.
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from dtreeplt import dtreeplt

iris = load_iris()
model = DecisionTreeClassifier()
model.fit(iris.data, iris.target)

dtree = dtreeplt(   model=model, feature_names=iris.feature_names, target_names=iris.target_names)
fig = dtree.view()
#if you want save figure, use savefig method in returned figure object.
#fig.savefig('output.png')

from dtreeplt import dtreeplt
dtree = dtreeplt()
dtree.view()
# If you want to use interactive mode, set the parameter like below.
dtree.view(interactive=True)
