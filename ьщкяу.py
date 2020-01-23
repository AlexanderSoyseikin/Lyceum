sp = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
      'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
      'o': '---', 'p':
          '.--.', 'q': '--.-',
      'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
      'y': '-.--', 'z': '--..',
      '.': '.', '-': '-', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
      '5': '.....',
      '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', " ": ""}


def encode_to_morse(text):
    for i in text.lower().split():
        print(' '.join(sp[j] for j in i), end=" ")



def main():
    print("1) Закодировать текст.")
    print("2) Декодировать текст")
    if input("Введите число - ") == "1":
        encode_to_morse(input("Введите текст."))
    else:
        decode_from_morse(input("Введите текст на азбуке морзе."))
    print("\n \n")

def decode_from_morse(code):
    string = ''
    for letter in code:
        for i in range(len(sp)):
            if letter == sp[i][1]:
                string += sp[i][0]
    print(string)

while True:
    main()

