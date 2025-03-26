char=input("enetr a character:").lower()
if len(char)==1:
 if char.isalpha():
    if char in ['a','e','i',"o","u"]:
        print("vowel letter")
    else:
        print("Consonants")
 else:
    print('special characters or non alphabets ')
else:
    print("Enter only less than 1 character")