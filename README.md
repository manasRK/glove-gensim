# glove-gensim
Converting GloVe vectors into word2vec format for easy usage with Gensim

word2vec embeddings start with a line with the number of lines (tokens?) and the number of dimensions of the file. This allows
gensim to allocate memory accordingly for querying the model. Larger dimensions mean larger memory is held captive. Accordingly, this line has to be inserted into the GloVe embeddings file.
