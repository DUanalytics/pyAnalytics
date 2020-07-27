#Topic: Decision Tree - Simple & iris
#-----------------------------
#libraries

from sklearn import tree
X = [[0, 0], [1, 1]]
Y = [0, 1]
X
Y
#X= features  which have labels as Y
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

#After being fitted, the model can then be used to predict the class of samples:
clf.predict([[2., 2.]])

#Alternatively, the probability of each class can be predicted, which is the fraction of training samples of the same class in a leaf:
clf.predict_proba([[2., 2.]])
#array([[0., 1.]])  # [probability of test being 0 is 0, being 1 is 1]


#Using the Iris dataset, we can construct a tree as follows:

from sklearn.datasets import load_iris
from sklearn import tree
X, y = load_iris(return_X_y=True)
X
y
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

#Once trained, you can plot the tree with the plot_tree function:
tree.plot_tree?
tree.plot_tree(clf) 

#We can also export the tree in Graphviz format using the export_graphviz exporter. If you use the conda package manager, the graphviz binaries and the python package can be installed with conda install python-graphviz.

#The export_graphviz exporter also supports a variety of aesthetic options, including coloring nodes by their class (or value for regression) and using explicit variable and class names if desired. Jupyter notebooks also render these plots inline automatically:
iris = load_iris()
iris.feature_names
iris.target_names

dot_data = tree.export_graphviz(clf, out_file=None,  feature_names=iris.feature_names,  class_names=iris.target_names, filled=True, rounded=True,  special_characters=True)  

import os
os.environ["PATH"] += os.pathsep + 'c:/Program Files (x86)/Graphviz2.38/bin/'

import graphviz 
from subprocess import call
call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])
     
graph = graphviz.Source(dot_data)  
graph 

#Alternatively binaries for graphviz can be downloaded from the graphviz project homepage, and the Python wrapper installed from pypi with pip install graphviz.
#Below is an example graphviz export of the above tree trained on the entire iris dataset; the results are saved in an output file iris.pdf:
import graphviz 
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("iris") 


#exporting tree in textual format
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
iris = load_iris()
decision_tree = DecisionTreeClassifier(random_state=0, max_depth=2) 
#changes this depth to get a bigger tree
decision_tree = decision_tree.fit(iris.data, iris.target)
r = export_text(decision_tree, feature_names=iris['feature_names'])
print(r)



#complete eg ..
