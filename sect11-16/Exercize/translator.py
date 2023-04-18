from translate import Translator

t = Translator(to_lang='ja')

try:
    with open('./test.txt', mode='r') as my_file:
        text = my_file.read()
        trans = t.translate(text)
        with open('./test-ja.txt', mode='w') as my_file2:
            my_file2.write(trans)
except FileNotFoundError as e:
    print('check file stupido')
