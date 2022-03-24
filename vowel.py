Description = "actress"
vowel = "aeiou"

sentence = f"Zendaya is a {Description} and musician from United States"
print(f"BEFORE:  {sentence}")

#split sentence 
word_list = sentence.split()

#find the index of the word
index_word_list = word_list.index(Actress) #3 
print(index_word_list)

#value = list[index]
letter = word_list[index_word_list]
print(letter)

#if start of letter is a vowel, word before is an 'an'
if letter[0] in vowel: 
    index_before = index_word_list - 1
    word_list[index_before] = "an"
    print(word_list)

#join the words together
testing = ' '.join(word_list)
print(testing)