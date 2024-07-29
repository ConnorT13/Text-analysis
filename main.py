from textblob import TextBlob
from newspaper import Article
import nltk

url = 'https://www.nbcnews.com/politics/2024-election/trump-harris-attacks-bum-failed-vice-president-rcna163922'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text) 

blob = TextBlob(text)
sentiment = blob.sentiment.polarity #-1 to 1

print(sentiment)

