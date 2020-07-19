# import gensim
# from utils import clean_str

# t_model = gensim.models.Word2Vec.load('pretrained_word_embeddings/wikipedia_cbow_100d/wikipedia_cbow_100')

# # python 3.X
# token = clean_str(u'ابو تريكه').replace(" ", "_")

# print(t_model.wv[u'ابو'])

# if token in t_model.wv:
#     most_similar = t_model.wv.most_similar( token, topn=10 )
#     for term, score in most_similar:
#         term = clean_str(term).replace(" ", "_")
#         if term != token:
#             print(term, score)
