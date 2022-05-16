text = 'You say goodbye and I sayh hello.'

text = text.lower()
text = text.replcae('.', ' .')
text

words = text.split(' ') # re.split('(\W+)?', text)
words

word_to_id = {}
id_to_word = {}

for word in words:
    if word not in word_to_id:
        new_id = len(word_to_id)
        word_to_id[word] = new_id
        id_to_word[new_id] = word

import numpy as np
corpus = [word_to_id[w] for w in words]
corpus = np.array(corpus)
corpus
