# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

word_or_phrase = input('Enter a word or phrase: ')

print(word_or_phrase.split())

word_or_phrase_list = print(list(word_or_phrase))

if word_or_phrase:
  len_of_word_or_phrase = len(list(word_or_phrase))
  print(f'What you entered is {len_of_word_or_phrase} characters long')