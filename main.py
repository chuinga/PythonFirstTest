number = 5
text = 'Hello World'
#print(number)
#print(text)
#print(text[6])
#print(text[-1])
#print(len(text))
#print(type(text))
shift = 3
#print(shift)
#print(type(shift))
alphabet = 'abcdefghijklmnopqrstuvwxyz'
#print(alphabet.find('z'))
index = alphabet.find(text[0])
index = alphabet.find(text[0].lower())
#print(index)
#print(text.lower())
shifted = alphabet[index+shift]
#print(shifted)
#print(shift)
text = 'Albatross'
for char in text.lower():    
    index = alphabet.find(char)
    print(char, index)
    new_index = index + shift