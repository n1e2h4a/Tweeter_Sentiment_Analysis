#Loading NLTK
import nltk
from nltk.tokenize import sent_tokenize


text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""
tokenized_text=sent_tokenize(text)
print(tokenized_text)
#Word Tokenization

from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(text)
print(tokenized_word)

#Frequency Distribution
from nltk.probability import FreqDist
fdist = FreqDist(tokenized_word)
print(fdist)
fdist.most_common(2)

# Frequency Distribution Plot
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

fdist.plot(30,cumulative=False)
plt.show()

