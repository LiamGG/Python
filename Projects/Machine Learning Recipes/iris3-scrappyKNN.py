from scipy.spatial import distance

# a - training data point, b - test data point
def euc(a,b):
	return distance.euclidean(a,b)

class ScrappyKNN():
	def fit(self, X_train, y_train):
		self.X_train = X_train
		self.y_train = y_train

	def predict(self, X_test):
		predictions = []
		for row in X_test:
			# method finds closest training mode to test point
			label = self.closest(row)
			predictions.append(label)
		return predictions

	def closest(self, row):
		best_dist = euc(row, self.X_train[0])
		best_index = 0
		for i in range(1, len(self.X_train)):
			dist = euc(row, self.X_train[i])
			if dist < best_dist:
				best_dist = dist
				best_index = i
		return self.y_train[best_index]

# import a dataset
from sklearn import datasets
iris = datasets.load_iris()

# features - x, labels - y (x is input, y is output => f(x) = y)
X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

# from sklearn import tree
# my_classifier = tree.DecisionTreeClassifier()

# from sklearn.neighbors import KNeighborsClassifier
# my_classifier = KNeighborsClassifier()

my_classifier = ScrappyKNN()

my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))
