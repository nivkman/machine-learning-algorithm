from sklearn import tree

features = [[1,2,3,4],[8,11,12,10],[1,7,4,3],[10,9,12,8],[13,10,9,11],[1,3,5,6],[10,9,12,8],[13,10,9,11],[1,3,5,6],[5,2,3,4],[1,2,3,4],[8,11,12,10],[1,7,4,3],[10,9,12,8],[13,10,9,11],[1,3,5,6],[10,9,12,8],[13,10,9,11],[1,3,5,6],[5,2,3,4]]
labels = ['backend', 'frontend', 'backend', 'frontend', 'frontend', 'backend', 'frontend', 'frontend', 'backend', 'backend','backend', 'frontend', 'backend', 'frontend', 'frontend', 'backend', 'frontend', 'frontend', 'backend', 'backend']

clf = tree.DecisionTreeClassifier()
i=0
while(i<10000):
    clf = clf.fit(features, labels)
    i+=1

print (clf.predict([[4,8,5,1]]))


# c: 1
# c++: 2
# java: 3
# js: 4
# node js: 5
# python: 6
# C#: 7

# react: 8
# angular: 9
# jQuery: 10
# bootstrap: 11
# HTML: 12
# matirial UI: 13
