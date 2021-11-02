def encrypt(phrase,shifts):
    words = phrase.split()
    cipher_words = []
    for word in words:
        cipher = ""
        for char in word:
            char_num = ord(char)
            if char_num<=90 and char_num >=65:
              shifted_num = char_num + shifts - 65
              mod_num = shifted_num % 26 + 65
              cipher += chr(mod_num)

            elif char_num<=122 and char_num >=97 :
              shifted_num = char_num + shifts - 97
              mod_num = shifted_num % 26 + 97
              cipher += chr(mod_num)

            else:
              cipher += char
        cipher_words.append(cipher)
    return " ".join(cipher_words)



def decrypt(phrase,shifts):
  return encrypt(phrase,-shifts)

import nltk, re
from nltk.corpus import words , names

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)
word_list = words.words()
name_list = names.words()

def count_words(text):
    words = text.split()
    word_count = 0
    for candidate_word in words:
        word = re.sub(r'[^A-Za-z]+','', candidate_word)
        if word.lower() in word_list or word in name_list:
            word_count += 1
    return word_count

def crack(phrase): 
    for key in range(0,27):
        new_phrase = decrypt(phrase,key)
        word_count = count_words(new_phrase)
        percentage = int(word_count / len(phrase.split()) * 100)
        if percentage > 90:
            return(new_phrase)   
