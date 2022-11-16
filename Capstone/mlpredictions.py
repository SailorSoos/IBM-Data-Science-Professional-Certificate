import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

#plotting the confusion matrix
def plot_confusion_matrix(y,y_predict):
    "this function plots the confusion matrix"
    from sklearn.metrics import confusion_matrix

    cm = confusion_matrix(y, y_predict)
    ax= plt.subplot()
    sns.heatmap(cm, annot=True, ax = ax); #annot=True to annotate cells
    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('True labels')
    ax.set_title('Confusion Matrix'); 
    ax.xaxis.set_ticklabels(['did not land', 'land']); ax.yaxis.set_ticklabels(['did not land', 'landed'])

data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/dataset_part_2.csv')
X = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/dataset_part_3.csv')

print(data.head())
print(X.head(100))

#TODO 1
#create a numpy array from the column class in data, and assign it to Y, 

#TODO 2 
#standardize the data in x then reassign it to the variable x using the transform provided below
# students get this 
transform = preprocessing.StandardScaler()

#TODO 3
#use the function train_test_split to split the data x and y into training and test data. Set the parameter test_size to
#0.2 and random_state to 2. The training data and test data should be assigned to the following labels. 
#X_train, X_test, Y_train, Y_test

# we can see we only have 18 test samples
Y_test.shape

#TODO 4
#create a logistic regression object then create a gridsearchCV object logreg_cv with cv=10
#fit the object to find the best parameters from the dictionary parameters
parameters ={'C':[0.01,0.1,1],
             'penalty':['l2'],
             'solver':['lbfgs']}

parameters ={"C":[0.01,0.1,1],'penalty':['l2'], 'solver':['lbfgs']}# l1 lasso l2 ridge
lr=LogisticRegression()

print("tuned hpyerparameters :(best parameters) ",logreg_cv.best_params_)
print("accuracy :",logreg_cv.best_score_)

#TODO 5 
#calculate the accuracy on the test data using the method score



yhat=logreg_cv.predict(X_test)
plot_confusion_matrix(Y_test,yhat)

#TODO 6
#create a support vector machine object then create a GridSearchCV object svm_cv with cv-10. Fit the object to 
#find the best parameters from the dictionary parameters. 
parameters = {'kernel':('linear', 'rbf','poly','rbf', 'sigmoid'),
              'C': np.logspace(-3, 3, 5),
              'gamma':np.logspace(-3, 3, 5)}
svm = SVC()


print("tuned hpyerparameters :(best parameters) ",svm_cv.best_params_)
print("accuracy :",svm_cv.best_score_)

#TODO 7 
#calculate the accuracy on the test data using the method score


#we can plot the confusion matrix
yhat=svm_cv.predict(X_test)
plot_confusion_matrix(Y_test,yhat)

#TODO 8 
#create a decision tree classifier object then create a GridSearchCV object tree_sv with cv=10. Fit the object to 
#find the best parameters form the dictionary parameters. 
parameters = {'criterion': ['gini', 'entropy'],
     'splitter': ['best', 'random'],
     'max_depth': [2*n for n in range(1,10)],
     'max_features': ['auto', 'sqrt'],
     'min_samples_leaf': [1, 2, 4],
     'min_samples_split': [2, 5, 10]}

tree = DecisionTreeClassifier()

#the todo goes here

print("tuned hpyerparameters :(best parameters) ",tree_cv.best_params_)
print("accuracy :",tree_cv.best_score_)

#TODO 9
#calculate the accuracy of tree_cv on teh test data using the method score4



#we can plot the confusion matrix
yhat = svm_cv.predict(X_test)
plot_confusion_matrix(Y_test,yhat)

#TODO 10
#create a k nearest neighbours object then create a GridSearchCV object knn_cv with cv = 10. Fit the object to find
#the best parameters form the dictionary parameters. 
parameters = {'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
              'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
              'p': [1,2]}

KNN = KNeighborsClassifier()

#the todo item goes in here


print("tuned hpyerparameters :(best parameters) ",knn_cv.best_params_)
print("accuracy :",knn_cv.best_score_)


#TODO 11
#calculate the accuracy of tree_cv on the test data using the method score



#we can plot the confusion matrix
yhat = knn_cv.predict(X_test)
plot_confusion_matrix(Y_test,yhat)

#TODO 12
#find the method that performs best



print("That's all!!!")




