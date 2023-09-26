import nltk
from textblob import TextBlob #sentiment analysis
from newspaper import Article #article scraping 
from gui import * #importing the gui file


nltk.download('punkt')

def summ():

    url=utext.get('1.0', "end").strip()

    article = Article(url)

    article.download()
    article.parse()

    article.nlp() #simplified way of using nlp from the libraries

    print(f'Title: {article.title}')
    print(f'Authors: {article.authors}')
    print(f'Publication Date: {article.publish_date}')
    print(f'Summary: {article.summary}')
    #print(f'Keywords: {article.keywords}')

    title.config(state='normal')
    author.config(state='normal')
    pub_date.config(state='normal')
    summary.config(state='normal')
    senti.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    pub_date.delete('1.0', 'end')
    pub_date.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)    
    senti.delete #sentiment analysis
    senti.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')
    #it checks the polarity of the text and if it is positive, negative or neutral,


    title.config(state='disabled')
    author.config(state='disabled')
    pub_date.config(state='disabled')
    summary.config(state='disabled')
    senti.config(state='disabled')


    analysis = TextBlob(article.text)    
    print(analysis.polarity) #sentiment analysis
    print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')
    #it checks the polarity of the text and if it is positive, negative or neutral,


