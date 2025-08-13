# MANUAL https://scikit-learn.org/0.21/tutorial/basic/tutorial.html
from sklearn import datasets




if __name__ == '__main__':

  """
  You can upload predefined data set 
  The data set is always in 2d ARRAY (n_samples, n_features)
  Exist variuos command target ( label that you point)
  """
  digits = datasets.load_digits()
  print(digits.data)
  digits.images[0]
  digits.target

