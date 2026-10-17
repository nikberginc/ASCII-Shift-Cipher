#simple veriable that is used in checking every letter in a sentens
i = 0



#this is for a testing purpeses so DELETE IT AFTER CREATING A GUI
user_word = input("Type your sentens so we can encrypt it\n")

#converst the users sentens to a list for eazyer convertion
user_word_list = list(user_word) 


#will go throu every word and changed it by - 13 places
while True:
    try:
        one_letter = user_word_list[i]
        one_letter_ASCII = ord(one_letter)

        #checks if the number in ASCII tabel is in between  32 and or is127
        if one_letter_ASCII <32 or one_letter_ASCII > 127:
            print("Error: input isnt between 32 and 127 in ASCII tabel")

        else:
            #will skip spaces
            if one_letter_ASCII == 32:
                i = i + 1
                continue
                

            one_letter_encryption = chr((one_letter_ASCII - 13 -33)%95 + 33)
            user_word_list[i] = one_letter_encryption
            encrypted_word = "".join(user_word_list)

    except IndexError:
        break


    i = i + 1


try:
    print(f"\n{encrypted_word}")
except NameError:
    print("you didnt type anything")