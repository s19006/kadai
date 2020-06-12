def ngram(sentence, n):
    return [sentence[x:x+n] for x in range(len(sentence) - n + 1)]

sentence = 'I am an NLPer'
print(ngram(sentence, 2))

words = sentence.split("a")
print(ngram(sentence, 3))
