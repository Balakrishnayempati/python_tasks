letter=(str(input("Enter any letter:")).lower())
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print(letter,"letter is vowel")
elif letter == "b" or letter == "c" or letter == "d" or letter == "f" or letter == "g":
    print(letter,"letter is consonant")
else:
    print(letter,"letter is not vowel&consonant")