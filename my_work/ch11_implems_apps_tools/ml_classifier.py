"""
Hello classifier
================
This text classifier will predict whether a given text carries a negative or positive connotation.
Before this can be done, we need to train our algorithm (model) with some data.

The naive Bayes model:
- useful in predicting the class of an unknown dataset; suited for text classification.
- Algorithms based on naive Bayes models are generally fast & produce accurate results.
- The whole model is based on the assumption that features are independent from each other.

To accurately predict the occurrence of rainfall, three conditions need to be considered: wind speed, temperature, and
the amount of humidity in the air. In reality, these factors do have an influence on each other to tell the likelihood
of rainfall. But the abstraction in naive Bayes is to assume that these features are unrelated in any way and thus
independently contribute to chances of rainfall.


Success on this simplistic examples still doesn't promise that if given the right amounts of data and a suitable
algorithm or model, it is possible for a machine to carry out tasks without any human help.

The specialized class NaiveBayesClassifier also did some heavy lifting for us in the background so we could not
appreciate the innards by which the algorithm arrived at the various predictions. """


# Hello classifier.
# After we have trained our mode, its prediction will fall into either the positive or negative category

from textblob.classifiers import NaiveBayesClassifier

#  each tuple holds the actual training data: (the sentence, the group it is associated with)
train = [
            ('I love this sandwich.', 'pos'),
            ('This is an amazing shop!', 'pos'),
            ('We feel very good about these beers.', 'pos'),
            ('That is my best sword.', 'pos'),
            ('This is an awesome post', 'pos'),
            ('I do not like this cafe', 'neg'),
            ('I am tired of this bed.', 'neg'),
            ("I can't deal with this", 'neg'),
            ('She is my sworn enemy!', 'neg'),
            ('I never had a caring mom.', 'neg')
]

# to train our model
cl = NaiveBayesClassifier(train)

# The updated naive Bayesian model cl will predict the category (pos/neg) that an unknown sentence belongs to.
print(cl.classify("I just love breakfast"))
print(cl.classify("Yesterday was Sunday"))
print(cl.classify("Why can't he pay my bills"))
print(cl.classify("They want to kill the president of Bantu"))

