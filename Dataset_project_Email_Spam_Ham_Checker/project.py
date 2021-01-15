from nltk.tokenize import RegexpTokenizer, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


df = pd.read_csv('./spam.csv', encoding='ISO-8859-1')
le = LabelEncoder()

data = df.to_numpy()
y = data[:, 0]
X = data[:, 1]
X.shape, y.shape

tokenizer = RegexpTokenizer('\w+')
sw = set(stopwords.words('english'))
ps = PorterStemmer()

def getStemmedReview(review):
    review = review.lower()
    
    # tokenize
    tokens = tokenizer.tokenize(review)

    # removing the stopwords
    new_tokens = [token for token in tokens if token not in sw]
    
    # stemming
    stemmed_tokens = [ps.stem(token) for token in new_tokens]
    
    cleaned_review = ' '.join(stemmed_tokens)

    return cleaned_review


def getStemmedDocument(document):
    d = []
    for doc in document:
        d.append(getStemmedReview(doc))
    return d

stemmed_document = getStemmedDocument(X)

stemmed_document[:10]

cv = CountVectorizer()
vectorized_corpus = cv.fit_transform(stemmed_document)
X = vectorized_corpus.todense()

X_train, X_test, y_train, y_test = train_test_split(
   X, y, test_size=0.33, random_state=42)



model = MultinomialNB()
model.fit(X_train, y_train)

model.score(X_test, y_test)

messages = [
    """
Hi Aakil,
We invite you to participate in MishMash - India’s largest online diversity hackathon. 
The hackathon is a Skillenza initiative and sponsored by Microsoft, Unity, Unilever, Gojek, Rocketium and Jharkhand Government. 
We have a special theme for you - Deep Tech/Machine Learning - sponsored by Unilever, which will be perfect for you.""",
    
    
    """Join us today at 12:00 PM ET / 16:00 UTC for a Red Hat DevNation tech talk on AWS Lambda and serverless Java with Bill Burke.
Have you ever tried Java on AWS Lambda but found that the cold-start latency and memory usage were far too high? 
In this session, we will show how we optimized Java for serverless applications by leveraging GraalVM with Quarkus to 
provide both supersonic startup speed and a subatomic memory footprint.""",

    """We really appreciate your interest and wanted to let you know that we have received your application.
There is strong competition for jobs at Intel, and we receive many applications. As a result, it may take some time to get back to you.
Whether or not this position ends up being a fit, we will keep your information per data retention policies, 
so we can contact you for other positions that align to your experience and skill set.
"""
]

def prepare_message(messages):
    d = getStemmedDocument(messages)
    # very very import, dont do fit_transform!
    return cv.transform(d)

messages = prepare_message(messages)

y_pred = model.predict(messages)

print(y_pred)