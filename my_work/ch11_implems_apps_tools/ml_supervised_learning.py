"""
A supervised learning example
=============================
- Assume that we have a set of posts to categorize.
With supervised learning, first train the model in order for it to accurately predict the category of an unknown post.

Example of supervised learning.
-------------------------------
We started by loading posts whose categories are already known.
These posts were then fed into the ML algorithm most suited for text processing based on the naive Bayes theorem.
A set of test post fragments were supplied to the model and the category was predicted.

Gathering data
--------------
The scikit module comes with a number of sample data; use newsgroups posts for training our model & load the  posts.

Bag of words
------------
The bag of words is a model that is used for representing text data in such a way that it does not take into
consideration the order of words but rather uses word counts to segment words into regions.

The bag of words enables us to decompose text into numerical feature vectors represented by a matrix.
This set((sentence_1 + sentence_2).split(" ")) will become our columns in the matrix.
The rows in the matrix will represent the documents that are being used in training.
The intersection of a row and column will store the number of times that word occurs in the document.

The preceding data alone will not enable us to predict accurately the category that new documents or articles will
belong to. The table has some inherent flaws. There may be situations where longer documents or words that occur in many
of the posts reduce the precision of the algorithm. Stop words can be removed to make sure only relevant data is
analyzed. Stop words include is, are, was, and so on. Since the bag of words model does not factor grammar into its
analysis, the stop words can safely be dropped. It is also possible to add to the list of stop words that one feels
should be exempted from final analysis.


Prediction
----------
- To test whether our model has learned enough to predict the category that an unknown post is likely to belong to.
"""
from sklearn.datasets import fetch_20newsgroups

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB


# I. Gathering data
# After training the model, the results of a prediction must belong to one of the following categories:
categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']

# use the newsgroups posts from sklearn and load them
training_data = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)

# print(training_data)

# The number of records we are going to use as training data
print(len(training_data))

# ML  algorithms don't mix well with textual attributes
# => the categories that each post belongs to are presented as numbers:
print(training_data.target)

# The categories have integer values that we can map back to the categories themselves
print(training_data.target_names[0])

# Now that the training data has been obtained, we must feed the data to a machine learning algorithm.


# II. Bag of words
sentence_1 = "As fit as a fiddle"
sentence_2 = "As you like it"
# To reduce our 2 sentences into the bag of words model, obtain a unique list of all the words:
set((sentence_1 + sentence_2).split(" "))

# To generate the values that go into the columns of our matrix, we have to tokenize our training data:
count_vect = CountVectorizer()
#  The training_matrix holds all the unique words and their respective frequencies.
training_matrix = count_vect.fit_transform(training_data.data)

# To mitigate the problem of basing prediction on frequency count alone & smooth out the inaccuracies in our data:
matrix_transformer = TfidfTransformer()
tfidf_data = matrix_transformer.fit_transform(training_matrix)
print(tfidf_data[1:4].todense())

# MultinomialNB is a variant of the naive Bayes model
model = MultinomialNB().fit(tfidf_data, training_data.target)


# III. Prediction - test whether our model has learned enough to predict the category
test_data = ["My God is good", "Arm chip set will rival Intel"]
# to obtain the vectorized form of the test data:
test_counts = count_vect.transform(test_data)
# To obtain the term frequency--inverse document frequency representation of the test dataset:
new_tfidf = matrix_transformer.transform(test_counts)

# To predict which category the docs may belong to:
prediction = model.predict(new_tfidf)

# Iterate over the prediction, showing the categories they are predicted to belong to:
for doc, category in zip(test_data, prediction):
    print('%r => %s' % (doc, training_data.target_names[category]))

# When the loop has run to completion, the phrase, together with the category that it may belong to, is displayed.
