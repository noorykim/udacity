def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    ### create classifier
    clf = GaussianNB()

    ### fit the classifier on the training features and labels
    trained = clf.fit(features_train, labels_train)

    ### use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)


    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example, 
    ### where we just print the accuracy
    ### you might need to import an sklearn module
    
    
    
    ## Method1
    
    diff = [x1 - x2 for (x1, x2) in zip(labels_test, pred)]
    diff2 = [x**2 for x in diff]
    
    noff = sum(diff2)
    print(noff)
    
    nelem = len(diff2)
    print(nelem)
    
    accuracy = 1 - noff/nelem
    
    
    ## Method 2
    from sklearn import accuracy_score
    print(accuracy_score(pred, labels_test))
    
    
    
    
    return accuracy
