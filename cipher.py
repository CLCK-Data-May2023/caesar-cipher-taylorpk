letters = 'abcdefghijklmnopqrstuvwxyz'

sentence = input('Please enter a sentence: ')
sentence= sentence.lower()

cipher = ''

for char in sentence:
    if char in letters: 
      index = letters.find(char)
      index = index + 5
      if index > 25:
        index -= 26
      char = letters[index]
    cipher += char

print('The encrypted sentence is:', cipher)