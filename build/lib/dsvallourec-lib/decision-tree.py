from sklearn.tree import DecisionTreeClassifier


def train_decision_tree(X_treinamento, y_treinamento, criterion='entropy', random_state=0):
    tree = DecisionTreeClassifier(criterion=criterion, random_state=random_state)
    tree.fit(X_treinamento, y_treinamento)
    return tree

def print_teste(teste):
    print(teste)
