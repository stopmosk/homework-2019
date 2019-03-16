import random
from hangman_logic import generate_string, check_letter, print_word


word_list = ['пистон', 'крыса', 'багор', 'революционер', 'мамлюк', 'беспредел']
random.seed()
word = random.choice(word_list)
attempts = len(word) + 33 // (len(word) + 1)  # Тупая формула, но пусть будет
exist_letters = set()

while attempts >= 0:
    if attempts == 0:
        print('Вы проиграли, я выливаю ваше вино в раковину. ', end='')
        print('Загаданное слово было "' + word + '".')
        break
    print_word(generate_string(word, exist_letters))
    print('У вас ' + str(attempts) + ' попыток')
    choice_letter = ''
    while not check_letter(exist_letters, choice_letter):
        choice_letter = input('\n Введите букву: ')
        print()
    exist_letters.add(choice_letter.lower())
    if generate_string(word, exist_letters) == word:
        print_word(word)
        print('Поздравляем, вы выиграли!')
        break
    attempts -= 1
