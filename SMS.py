import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.naive_bayes import MultinomialNB
	
def predict(message):
    
    # Load Data
	df = pd.read_csv('spamraw.csv')
	df.head()
	data_train, data_test, labels_train, labels_test = 	train_test_split(df.text,df.type,test_size=0.2,random_state=0) 
	vectorizer = CountVectorizer()
	
	#fit & transform
	data_train_count = vectorizer.fit_transform(data_train)
	data_test_count  = vectorizer.transform(data_test)
	clf = MultinomialNB()
	clf.fit(data_train_count, labels_train)
	result = clf.predict(vect)
	return result
