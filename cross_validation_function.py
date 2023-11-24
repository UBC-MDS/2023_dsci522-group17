# Imports
import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate

# Test data
X_train = pd.DataFrame(np.ones((10,1)))
y_train = pd.DataFrame([['yes'],['yes'],['yes'],['yes'],['yes'],
                       ['yes'],['yes'],['yes'],['yes'],['no'],])
y_train







model_dict = {
    "dummy": DummyClassifier(random_state=123), 
    "Decision Tree": DecisionTreeClassifier(random_state=123),
    "KNN": KNeighborsClassifier(),
    "RBF SVM": SVC(random_state=123),
    "Naive Bayes": GaussianNB(),
    "Logistic Regression": LogisticRegression(max_iter=2000, multi_class="ovr", random_state=123),
}

def cross_val_by_model(model_dict, X_train, y_train, **kwargs):
    results = pd.DataFrame()
    for name, model in model_dict.items():
        scores = cross_validate(model, X_train, y_train, return_train_score=True)

        mean_scores = pd.DataFrame(scores).mean()
        std_scores = pd.DataFrame(scores).std()
        out_col = []

        for i in range(len(mean_scores)):
            out_col.append((f"%0.3f (+/- %0.3f)" % (mean_scores[i], std_scores[i])))

        
        results[name] = pd.Series(data=out_col, index=mean_scores.index)
    return results

cross_val_by_model(model_dict, X_train, y_train)