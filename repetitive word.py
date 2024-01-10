import re

def firstRepeatedWord(s):
    words = re.split('[\s,;.:-]+', s.lower())
    word_count = {}

    for word in words:
        if word == '':
            continue
        if word in word_count:
            return word
        word_count[word] = 1

    return None 

user_input = input("Lütfen bir cümle giriniz: ")

print("İlk tekrar eden kelime:", firstRepeatedWord(user_input))
