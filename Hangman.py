import random
import hangmanArt

print(hangmanArt.logo)
len_man = len(hangmanArt.stages) - 1

word = random.choice(hangmanArt.word_list).lower()                         # choose word
guessing_word = ['_' for i in range(len(word))]                 # get guessing line (___)
a = guessing_word.count('_')

while guessing_word.count('_') and len_man:

    print(hangmanArt.stages[len_man])
    print(''.join(guessing_word))
    letter = input('enter letter in order to find: ').lower()

    for i in range(len(word)):
        if letter == word[i]:                       # that checks  letter is correct
            guessing_word[i] = word[i]


    if guessing_word.count('_') == a:               # if letter not correct you lost chance
        len_man -= 1

    a = guessing_word.count('_')


if not guessing_word.count('_'):
    print(f'you won game\n\n\n' + ''.join(guessing_word))
else:
    print(f'{hangmanArt.stages[len_man]}\n\n you lost game')

