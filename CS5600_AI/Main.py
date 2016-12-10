"""
Matthew McGary

Main.py contains methods for utilizing various
learning algorithms. Refer to each function for more
information. Code correlation was drawn from the original idea from
https://github.com/patrickshao. Most functions used are from scikit
http://scikit-learn.org/stable/supervised_learning.html#supervised-learning.
Data was drawn from football-data.co.uk. To run this program, first run LoadCSV.py
then run Main.py to test the results and accuracies.
"""

import numpy as np

def gauss(trainingData,trainingLabels):
    """
    Implements a Gaussian Bayes Classifier to take in
    the training data/labels and returns a classifier.
    """

    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(trainingData,trainingLabels)
    GaussianNB()

    print "Gaussian Naive Bayes Classifier has been generated with a training set size of ",len(trainingLabels) ,"."
    return clf

def multi(trainingData,trainingLabels):
    """
    Uses Multinomial Naive Bayes, which takes in 
    training data in the form of vectors, and returns a
    classifier. Note: The size of trainingLabels and 
    trainingData should bethe same size
    """

    #Check to ensure same size
    if not(len(trainingLabels) == len(trainingData)):
        print "Error: Labels and Data are of different sizes: cannot train."
        return

    #Import from scikit and fit the data into the algorithm
    from sklearn.naive_bayes import MultinomialNB
    clf = MultinomialNB()
    clf.fit(trainingData, trainingLabels)
    MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)

    print "Multinomial Naive Bayes Classifier has been generated with a training set size of ",len(trainingLabels) ,"."
    return clf

def svm(trainingData,trainingLabels):
    """
    Uses Support Vector Machine (SVM) as the algorithm as
    the classifier. The 'kernel' param is used to determine
    which kernel function to use. Currently using rbf, the default.
    Doesn't work as effectively when there are too many training samples
    or too many features.
    """
    #Check to ensure same size
    if not(len(trainingLabels) == len(trainingData)):
        print "Error: Labels and Data are of different sizes: cannot train."
        return
    #Import svm from scikit and fit the data into the classifier
    from sklearn.svm import SVC
    k = 'rbf'
    clf = SVC(kernel='rbf')
    clf.fit(trainingData, trainingLabels)  

    print "Support Vector Classifier with kernel:", k," has been generated with a training set size of",len(trainingLabels)
    return clf

def perceptron(trainingData,trainingLabels):
    """
    Implements a linear perceptron model as the
    machine learning algorithm.
    """
    from sklearn.linear_model import Perceptron
    clf = Perceptron()
    clf.fit(trainingData,trainingLabels)
    
    print "Perceptron has been generated with a training set size of",len(trainingLabels)
    return clf

def sgdClassifier(trainingData,trainingLabels):
    """
    Implements Stochastic Gradient Descent as a classifier
    to use as the learning algorithm. Works best if there is
    a lot of training data and a lot of features.
    """
    from sklearn.linear_model import SGDClassifier
    clf = SGDClassifier(loss="hinge", penalty="l2")
    clf.fit(trainingData, trainingLabels)
    
    print "Stochastic Gradient Descent Classifier generated with a training set size of",len(trainingLabels)
    return clf



def predict(clf, newData):
    """
    Takes in a classifier and data and returns a prediction
    """
    return clf.predict(newData)

#Less efficient version of testAccuracy
def testAccuracy(clf,validationData,validationLabels):
    """
    Given a declared classifier and validation data, run the
    classifier on these sample values and record the accuracy.
    Prints out the final accuracy at the end and returns it.
    """
    size = len(validationLabels)
    correct = 0.0
    for x in range(size):
        tru = validationLabels[x]
        est = clf.predict(validationData[[x]])
        if int(est) == int(tru):
            correct += 1

    accuracy = correct/size
    print "Number correct:", correct, "out of", size,"; Accuracy:", accuracy*100, "%"
    return accuracy


def extractFile(filename):
    """
    Returns a tuple of the trainingLabels and the trainingData.
    Assumes that the first value of each row is the label.
    """
    dataset = np.loadtxt(filename, delimiter=",")
    tempData = []
    tempLabels = []
    for x in range(len(dataset)):
        tempLabels.append(dataset[x][0])
        tempData.append(dataset[x][1:])
    return (np.array(tempData),np.array(tempLabels))

def chooseClassifier(switch, trainingData,trainingLabels):

    if switch == 1:
        return gauss(trainingData,trainingLabels)
    if switch == 2:
        return multi(trainingData,trainingLabels)
    if switch == 3:
        return svm(trainingData,trainingLabels)
    if switch == 4:
        return perceptron(trainingData,trainingLabels)
    if switch == 5:
        return sgdClassifier(trainingData,trainingLabels)
        
        
#Testing code 
(data,labels) = extractFile("train.csv")
(valData,valLabels) = extractFile("test.csv")
clf = chooseClassifier(1,data,labels)
testAccuracy(clf,valData,valLabels)
clf = chooseClassifier(2,data,labels)
testAccuracy(clf,valData,valLabels)
clf = chooseClassifier(3,data,labels)
testAccuracy(clf,valData,valLabels)
clf = chooseClassifier(4,data,labels)
testAccuracy(clf,valData,valLabels)
clf = chooseClassifier(5,data,labels)
testAccuracy(clf,valData,valLabels)