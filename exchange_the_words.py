def reverseWordSentence(Sentence):
    words = Sentence.split(" ")
    newWords = words[::-1]
    newSentence = " ".join(newWords)
    return newSentence
Sentence =input()
print(reverseWordSentence(Sentence))