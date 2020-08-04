#Topic:Visualising Decision Tree in Python
#-----------------------------
#libraries

#4 ways
# sklearn.tree.export_text
# sklearn.tree.plot_tree (matplot needed)
# skearn.tree.export_graphviz  (graphviz needed)
# dtreeviz package (dtreeviz and graphvis needed)


import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

iris = datasets.load_iris()
X = iris.data
y = iris.target
iris.feature_names

clf = DecisionTreeClassifier(random_state=1234)
model = clf.fit(X,y)

#print representation
text_representation = tree.export_text(clf)
print(text_representation)
#save to a file
with open('decisiontree1.log','w') as fout :    fout.write(text_representation)

#plottree
tree.plot_tree(decision_tree=clf)

fig = plt.figure(figsize=(10,8))
_ = tree.plot_tree(clf, feature_names= iris.feature_names, class_names=iris.target_names, filled=True)  #see plot

import graphviz
dot_data = tree.export_graphviz(decision_tree=clf, out_file=None, feature_names = iris.feature_names, class_names = iris.target_names, filled=True)
graph = graphviz.Source(dot_data, format='png')
#error dot path
import os
os.environ["PATH"] += os.pathsep + 'c:/Program Files (x86)/Graphviz2.38/bin/'
graph = graphviz.Source(dot_data, format='png')
graph
graph.render('DecisionTree.png ')


#%%%Plot DT with dtreeviz
#pip install dtreeviz
from dtreeviz.trees import dtreeviz
viz = dtreeviz(clf, X,y, target_name='target', feature_names = iris.feature_names, class_names = list(iris.target_names))
viz
viz.save('dt2.svg')

