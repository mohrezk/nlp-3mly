# from nltk.tokenize import word_tokenize, sent_tokenize

# text = "my name is mohamed. I am a cs student. 22 years old"

# words = word_tokenize(text)
# print(words)

# sentences = sent_tokenize(text)
# print(sentences)

# words_using_split = text.split()
# print(words_using_split)

#=============================================================================

# from nltk.stem import PorterStemmer as p_stem, SnowballStemmer as s_stem

# words = [
#     "bags", "computer", "dogs", "generous", "kites", "veins", "photos", "natives", "traditional", "mice"
# ]

# p_stemmer = p_stem()
# for word in words:
#     print(p_stemmer.stem(word))

# print(s_stem.languages)

# s_stemmer = s_stem(language="english")
# for word in words:
#     print(s_stemmer.stem(word))


#=============================================================================

# from nltk import ngrams

# text = "my name is mohamed. i am a cs student."

# grams = ngrams(text.split(), 2)

# for gram in grams:
#     print(gram)

#=============================================================================

# import spacy 

# nlp = spacy.load("en_core_web_sm")

# text = "my name is mohamed. i am a cs student"

# text_doc = nlp(text)

# for sentence in text_doc.sents:
#     print(sentence.text)

# for word in text_doc:
#     print(word.text)


#=============================================================================

# from nltk.tokenize import word_tokenize as w_tok
# from nltk import pos_tag
# from nltk.corpus import brown

# print(brown.tagged_words()[:5])

# text = "my name is mohamed"
# words = w_tok(text)

# print(pos_tag(words, tagset="universal"))

# print(pos_tag(words, tagset="treeback"))


#=============================================================================

import spacy 

nlp = spacy.load("en_core_web_sm")

text = "my name is mohamed."

text_doc = nlp(text)

print(text_doc[1].vector)