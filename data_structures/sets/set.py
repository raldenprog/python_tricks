vowels = {'а', 'о', 'э', 'и', 'у', 'ы', 'е', 'е', 'ю', 'я'}
print('э' in vowels)
# True
letters = set('алиса')
print(letters.intersection(vowels))
# {'а', 'и'}
vowels.add('х')
print(vowels)
# {'х', 'о', 'э', 'у', 'и', 'ы', 'е', 'е', 'ю', 'а', 'я'}
print(len(vowels))
# 6
