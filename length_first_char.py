#!/usr/bin/python3
# return length of a sentence and its first character
def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    elif len(sentence) > 0:
        return len(sentence), sentence[0]

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
