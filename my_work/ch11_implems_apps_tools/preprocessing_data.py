"""
Implementations, Applications, and Tools
=========================================

Algorithms real-life application - data structures and algorithms are shaping our world.

- The abundance of data - E-mails, phone numbers, text, and image documents contain large amounts of data. In this data
is found valuable information that makes the data become more important. But to extract this information from the raw
data, we will have to use data structures, processes, and algorithms specialized for this task.

Machine learning employs a significant number of algorithms to analyze and predict the occurrence of certain variables.
Analyzing data on a purely numerical basis still leaves much of the latent information buried in the raw data.
Presenting data visually thus enables one to understand and gain valuable insights too.

Goal:
Prune and present data accurately
Use both supervised and unsupervised learning algorithms for the purposes of prediction
Visually represent data in order to gain more insight


Tools of the trade
==================
Install these packages - will be used to preprocess and visually represent the data being processed.
Some of the packages also contain well-written and perfected algorithms that will operate on our data.

Preferably, these modules should be installed within a virtual environment such as pip.
These packages may require other platform-specific modules to be installed first. Install all dependencies.

% pip install numpy
% pip install scikit-learn
% pip install matplotlib
% pip install pandas
% pip install textblob


Numpy:        A library with functions to operate on n-dimensional arrays and matrices.
Scikit-learn: A highly advanced module for ML; contains a good number of algorithms for classification, regression,
              and clustering, among others.
Matplotlib:   A plotting library that makes use of NumPy to graph a good variety of charts, including line plots,
              histograms, scatter plots, and even 3D graphs.
Pandas:       This library deals with data manipulation and analysis.


Data preprocessing - use NumPy and pandas
==================
Collection of data from the real world is fraught with massive challenges. The raw data collected is plagued with a lot
of issues, so much so that we need to adopt ways to sanitize the data to make it suitable for use in further studies.

Q. Why process raw data?
A. Raw data as collected from the field is rigged with human error. Data entry is a major source of error when
collecting data. Even technological methods of collecting data are not spared. Inaccurate reading of devices, faulty
gadgetry, and changes in environmental factors can introduce significant margins of errors as data is collected.

The data collected may also be inconsistent with other records collected over time. The existence of duplicate entries
and incomplete records warrant that we treat the data in such a way as to bring out hidden and buried treasure.
The raw data may also be shrouded in a sea of irrelevant data.

To clean the data up, totally discard irrelevant data (noise). Data with missing parts or attributes can be replaced
with sensible estimates. Where the raw data suffers from inconsistency, detecting & correcting them is necessary.

Missing data
------------
Data collection is tedious and, once data is collected, it should not be easily discarded. Just because a dataset has
missing fields/attributes doesn't mean it is not useful. Several methods can be used to fill up the nonexistent parts -
by either using a global constant, using the mean value in the dataset, or supplying the data manually.
The choice is based on the context and sensitivity of what the data is going to be used for.


Feature scaling
---------------
The columns in a data frame are known as its features. The rows are known as records or observations.

(check data2) Ideally, we will need to scale the data to a certain range in order to get consistent results.
Once again, a closer inspection reveals that each feature (or column) lies around different mean values.
Therefore, what we would want to do is to align the features around similar means. One benefit of feature scaling is
that it boosts the learning parts of machine learning => use the scikit module to apply scaling algorithms to the data.

Min-max scalar
--------------
The min-max scalar form of normalization uses the mean and standard deviation to box all the data into a range lying
between a certain min and max value. For most purposes, the range is set between 0 and 1. At other times, other ranges
may be applied but the 0 to 1 range remains the default.

Standard scalar
---------------

Binarizing data
---------------
To binarize a given feature set, we make use of a threshold. If any value within a given dataset is greater than the
threshold, the value is replaced by 1. If the value is less than the threshold 1, we will replace it.
"""

import numpy as np
import pandas
import sklearn
import matplotlib
import textblob


# NumPy and pandas for data preprocessing techniques

# the data elements data[1][0] and data[1][1] have values being np.NAN, i.e. they have no value.
# If the np.NAN values are undesired in a given dataset, they can be set to some constant figure.

data = pandas.DataFrame([
                          [4., 45., 984.],
                          [np.NAN, np.NAN, 5.],
                          [94., 23., 55.]
])
# set data elements with the value np.NAN to 0.1:
print(data.fillna(0.1))
# set data elements with the value np.NAN to the mean (calculated for each column):
print(data.fillna(data.mean()))


# Feature scaling
# data matrix:  For feature 2, with data 1, 200, 65, the data lies between 1 and 200 =>
# Inconsistent results will be produced if we supply this data to any machine learning algorithm.
# Ideally, we will need to scale the data to a certain range in order to get consistent results.
data2 = pandas.DataFrame([
                            [58., 1., 43.],
                            [10., 200., 65.],
                            [20., 75., 7.]
])

# Min-Max scalar
# An instance of the MinMaxScaler class is created with the range (0,1)

scaled_values = sklearn.preprocessing.MinMaxScaler(feature_range=(0,1))
results = scaled_values.fit(data).transform(data)
# all the data is normalized and lies between 0 and 1 => output can now be supplied to a ML algorithm
print(results)


# Standard scalar
# The mean values for the respective features in our initial dataset or table are 29.3, 92, and 38.
# To make all the data have a similar mean, that is, a zero mean and a unit variance across the data
stand_scalar = sklearn.preprocessing.StandardScaler()
results = stand_scalar.fit(data).transform(data)
# all our features are now evenly distributed.
print(results)


# Binarizing data
# 50.0 is the threshold that will be used in the binarizing algorithm
results = sklearn.preprocessing.Binarizer(50.0).fit(data).transform(data)
# All values in the data < 50 will have 0 in their stead. The opposite also holds true.
print(results)



