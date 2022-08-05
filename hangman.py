import random

def ahorcado():
    print('*' * 30)
    print('AHORCADO')
    print('*' * 30)
    words_lists = ('aire','ojos','piel','anteojos','joven','viejo','mate','zoologico','manicuria','cama','silla','mesa',
                   'tenedor','cuchillo','cuchara','colchon')
    word = list(random.choice(words_lists))
    lifes = 6
    word_complete = False
    word_success = ['_'] * len(word)
    words_fakes = []
    while lifes != 0:
        letter = input('Ingrese una letra: ').lower()
        if letter in word:
            for letra in range(len(word)):
                if letter == word[letra]:
                    word_success[letra] = letter
            print('La letra se encuentra en la palabra')
            print()
            print(word_success)
            if len(words_fakes ) != 0:
                print('Letras Incorrectas:',words_fakes)
            if word_success == word:
                word_complete = True
            if word_complete:
                print('GANASTE')
                break
        else:
            lifes -= 1
            print('La letra no se encuentra en la palabra')
            print()
            print()
            if letter not in words_fakes:
                words_fakes.append(letter)
            else:
                print('..Esta letra ya la elegiste...')
            print('Letras incorrectas: ',words_fakes)
            print('******** Te quedan ', lifes, ' vidas ********')

    else:
        print()
        print('La palabra correcta era: ',word)
        print()
        print('PERDISTE...Se te acabaron los intentos')



if __name__ == '__main__':
    ahorcado()