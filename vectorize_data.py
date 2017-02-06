import sys
import multiprocessing
import gensim
from gensim import models as md
file, text, model, vector = sys.argv[1: 4]
#firstly exctracting the information
data = gensim.corpora.WikiCorpus(file, lemmatize = False, dictionary = {}) #lemmatize is diabled since pattern could slow the process
for words in data.get_texts():
	output.write(" ".join(words) + "\n")
#the data is exctracted, clearing it completely of punctuation
#training the model using the data
data = output(text, 'r')
mod = md.Word2Vec(md.word2vec.LineSentence(data), size = 300, window = 5, min_count = 5, workers = multiprocessing.cpu_count())
mod.save(model)
mod.save_word2vec_format(vector, binary = False)