from textblob import TextBlob
from newspaper import Article
import nltk

url = 'https://en.wikipedia.org/wiki/Mathematics'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text) 

