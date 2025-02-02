def ubbi_dubbi(word):
    output = []
    for letter in word:
        if letter in 'aeoiu':
            output.append(f'ub{letter}')
        else:
            output.append(letter)
    return ' '.join(output)

print(ubbi_dubbi('python'))    

print(ubbi_dubbi('orange'))  