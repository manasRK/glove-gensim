import gensim

#word2vec embeddings start with a line with the number of lines (tokens?) and the number of dimensions of the file. This allows
#gensim to allocate memory accordingly for querying the model. Larger dimensions mean larger memory is held captive. Accordingly, this line
#has to be inserted into the GloVe embeddings file.

#GloVe Model File
#More models can be downloaded from http://nlp.stanford.edu/projects/glove/
fname="glove.6B.50d.txt"

#convert Glove vectors to word2vec format
word2vec_convert_file="word2vec_line.txt"

#to be a first line insert
num_lines = sum(1 for line in open(fname))
dims=50

print '%d lines with %d dimensions' %(num_lines,dims)

with open(word2vec_convert_file,'w') as f:
    f.write(str(num_lines)+ " " +str(dims) + '\n')
f.close()

model_file='glove_model.txt'

filenames = [word2vec_convert_file,fname]

with open(model_file, 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
outfile.close()    

#load converted model file                        
model=gensim.models.Word2Vec.load_word2vec_format(model_file,binary=False) #GloVe Model

print model.most_similar(positive=['australia'], topn=10)
print model.similarity('woman', 'man')
