
def romb(letter, all_letters):
    # not hardcoded

    # test cases assert
    # check type

    # не нашел способа применить try 

    # check is alfa
    find =all_letters.find(letter)

    all_letters = all_letters[:find+1]
    for char in all_letters:
        distance = find - all_letters.find(char)
        external = [' ' for _ in range(distance)]
        external = ''.join(external)

        internal = ['_' for _ in range(all_letters.find(char)*2 - 1)]
        internal = ''.join(internal)
        if all_letters.find(char) == 0:
            print(external+char+internal+external)
        else:
            print(external+char+internal+char+external)

    for char in all_letters[-2::-1] :
        distance = find - all_letters.find(char)
        external = [' ' for _ in range(distance)]
        external = ''.join(external)

        internal = ['_' for _ in range(all_letters.find(char)*2 - 1)]
        internal = ''.join(internal)
        if all_letters.find(char) == 0:
            print(external+char+internal+external)
        else:
            print(external+char+internal+char+external)

#==========================================================
#
# тут должна быть обработка вводимой буквы
# смотрим, в какой диапазон символов unicode входит
# брал тут - https://unicode-table.com/ru/
# и исходя из этого генерируем массив для ромба
# пока реализована латицица и кириллица.
# 
#==========================================================

def is_unicode (u_letter):
    assert len(u_letter) < 2, 'Только одна буква'
    assert u_letter.isalpha(), 'Ну букву же!'
    u_letter = u_letter.upper()
    un_array = ''
    in_let = ord(u_letter)

    if in_let >= 65 and in_let <= 90:
        for i in range ((90-65)+1):
            j = i + 65
            un_array = un_array + un_array.join(chr(j))
    elif in_let >= 1040 and in_let <= 1071:
        for i in range ((1071-1040)+1):
            j = i + 1040
            un_array = un_array + un_array.join(chr(j))
    else:
        print("Ерунда какая-то...")
        exit (0)
        
#    print (un_array)
    romb(u_letter, un_array )


in_letter = str(input ("Введите букву: "))
is_unicode(in_letter)

# IMHO лучше сразу проверять ввод, не передавая
# в функцию не то, что там ожидают...
# if len(in_letter) > 1:
#     print ("Одна буква!")
#     exit(0)
# elif not in_letter.isalpha():
#     print ("Ну букву же!")
#     exit(0)
# else:
#     in_letter = in_letter.upper()
# #    print (ord(in_letter))
# #    print(in_letter)
#     is_unicode(in_letter)
<<<<<<< HEAD

in_letter = in_letter.upper()
is_unicode(in_letter)
=======
>>>>>>> 1ac024f93bc38eaf3f6d7ca944febeffa0021af3
