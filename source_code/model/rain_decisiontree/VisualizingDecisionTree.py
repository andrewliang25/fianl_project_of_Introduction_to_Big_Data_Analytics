from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

def Visualize(decision_tree, feature_columns, class_feature):
    dot_data = StringIO()
    export_graphviz(decision_tree, out_file=dot_data,
                    filled=True, rounded=True,
                    special_characters=True, feature_names=feature_columns, class_names=class_feature)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_png('rainfall_tree.png')
    Image(graph.create_png())
