from embeddings import EmbeddingsDictionary

emb = EmbeddingsDictionary(max_words=200000,
				path='/Users/nmanzini/goinfre/wiki-news-300d-1M.vec',
                normalize=True,
                word_whitelist=None)

# print("index of'people'")
# print(emb.dictionary['people'])

# print("w2neighbors of 'people'")
# print(emb.w2neighbors('people',10))

# print("emb.words[65]")
# print(emb.words[65])

# print(emb.w2neighbors('geek',10))

# a = emb.emb[emb.dictionary['London']]
# b = emb.emb[emb.dictionary['day']]
# c = emb.emb[emb.dictionary['rain']]

# query = a + b - c

# _scores, lst_closest = emb.emb2neighbors(query)

# print("emb.emb2neighbors(query)")
# for word in lst_closest:
# 	print(emb.words[word],end=', ')

# # print("emb.words[4601]")
# # print(emb.words[4601])

# emb.analogy("youtube","cat","google")
# print()
# emb.analogy("phone","video","apple")
print()
emb.analogy("wine","france","italy")