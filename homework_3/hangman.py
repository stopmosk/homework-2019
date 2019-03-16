import random
from hangman_logic import generate_string, check_letter, print_word


word_list = ['пистон', 'крыса', 'багор', 'революционер', 'мамлюк', 'беспредел']
random.seed()
word = random.choice(word_list)
attempts = len(word) + 33 // (len(word) + 1)  # Тупая формула, но пусть будет
letters = set()

while attempts >= 0:
    if attempts == 0:
        print('Вы проиграли, я выливаю ваше вино в раковину. ', end='')
        print('Загаданное слово было "' + word + '".')
        break
    print_word(generate_string(word, letters))
    print('У вас ' + str(attempts) + ' попыток')
    let_in = ''
    while not check_letter(letters, let_in):
        let_in = input('\n Введите букву: ')
        print()
    letters.add(let_in.lower())
    if generate_string(word, letters) == word:
        print_word(word)
        print('Вы выиграли!')
        break
    attempts -= 1

