def romb(letter):
    # not hardcoded
    all_letters = 'abcdegfxyz'
    # test cases assert
    # check type

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

romb("d")
