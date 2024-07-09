from googletrans import Translator

def translate(text, src='de', dest='en'):
    translator = Translator()
    text_trans = translator.translate(text, src=src, dest=dest)
    return text_trans.text

def main():
    text = input('Enter a text: ')
    translated = translate(text)
    print(f"Your translated text: {translated}")

if __name__ == '__main__':
    main()
