import argparse
import pandas as pd
import numpy as np
import nltk

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import train_test_split
from nltk.tokenize import RegexpTokenizer

if __name__ == "__main__":

    # Parse inputs
        parser = argparse.ArgumentParser()
        parser.add_argument('--test', help = "test argument help", type = str, required=False)
        args = parser.parse_args()

    # Load datasets
        training_data = pd.read_csv('trainset-sentiment.csv', delimiter=',')
        pred_data = pd.read_csv('predictors.csv', delimiter=',')
        print("This is how data looks before tokenization: \n",pred_data.loc[[0]])

    # Descriptives
        #pred_data.info()
        #training_data.info()

        vec = TfidfVectorizer()

        text_counts = vec.fit_transform(training_data['textcat'])
        new_counts = vec.transform(pred_data['textcat'])

        print("This is how the same data looks after vectorization: \n", new_counts[0])
        
    # Split datasets
        X_train, X_test, y_train, y_test = train_test_split(text_counts, training_data['label'], test_size = 0.27, random_state = 1)

    # Train
        clf = MultinomialNB()
        clf.fit(X_train, y_train)

    # Evaluate
        predicted = clf.predict(X_test)
        accuracy = metrics.accuracy_score(predicted, y_test)
        print(str('{:04.2f}'.format(accuracy*100)) + '%')

    # Predict
        print(clf.predict(new_counts))




