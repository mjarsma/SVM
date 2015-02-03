# import sys
from time import time
# sys.path.append("/Users/Miikka/ud120-projects/tools/");
from email_preprocess import preprocess;
from sklearn.svm import SVC;
from sklearn.metrics import accuracy_score;

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess();
clf = SVC(kernel="rbf", C = 10000.);

features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

t0 = time();
clf.fit(features_train, labels_train);
print "training time:", round(time()-t0, 3), "s";
t1 = time();
pred = clf.predict(features_test);
print "predicting time:", round(time()-t1, 3), "s";

print accuracy_score(labels_test, pred);