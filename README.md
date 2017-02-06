# dbpedia-warm-up-task
<h2>Knowledge base embeddings for DBpedia</h2>
This python code trains word2vec embeddings using gensim and Wikipedia text + links.
Download the data from English Wikipedia 

https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2

The wiki data without punctuation is stored in wiki.txt

Model is stored in wiki.model using the save() method.

The vectorized data is stored in wiki.vector using the save_word2vec_format() method.

Example input:

```
python vectorize_data.py enwiki-latest-pages-articles.xml.bz2 wiki.txt wiki.model wiki.vector
```
