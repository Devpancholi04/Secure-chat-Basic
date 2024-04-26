import random
import string



def coding(): # here the coding function begin

    global coded_message # it was created as global because to use in decoding function

    message = input("enter your messsage  : ") # here we will take the message from user

    message = message.split() # it is used to spilt a string into list and single characters

    new_word = [] # here we have created a empty list to store coded values

    for messages in message:
        if(len(messages) <= 2):
            messages = messages[::-1] # it is used to swap the value of character if the length is less than 3

            new_word.append(messages) # it is used to add the element to new word list

        elif(len(messages) >= 3):

            a = list(messages) # it is used to typecast the string message to list

            po = a.pop(0) # it is used to remove first character from string 

            ad = a.append(po) # it is used to add perviously remove character to end

            listt =  string.ascii_lowercase # it used to get all the alpabhet character in lowercase using string function
            lists = list(listt) # it is used to typecasting all the string alpabhat to list

            ran1 = []
            for i in range(3):
                ra = random.choice(lists) # it is used to get the 3 random value 
                ran1.append(ra)

            ran2 = []
            for i in range(3): 
                ra = random.choice(lists) # it is used to get the 3 random value 
                ran2.append(ra)
            
            message1 = ran1 + a + ran2 # here we will add random character at the start and at the end with swaped value element to code the message 

            message2 = "".join(message1) # it is used to merge all character and make a single string
            new_word.append(message2) # it is used to add element to new word list

    coded_message = " ".join(new_word) # it is used to merge all the coded element to string
    print('\n', coded_message ,'\n')



def decoding(): # here decoding function starts

    new_word = [] # here we have created a empty list to store decoded values

    message = coded_message.split() # it is used to spilt a string into list and single characters   

    for messages in message:
        if(len(messages) <= 2):
            messages = messages[::-1] # it is used to swap the value of two characters
            new_word.append(messages) # it is used to add elements in new word list
            # print(new_word)

        elif(len(messages) >= 3):
            messages = list(messages) # it is used to typecasting string message to list

            for i in range(0,3):
                messages.pop(0) # it is used to remove 3 character from starting which was a random characters
                messages.pop(-1) # it is used to remove 3 character from last which was a random characters
            
            po = messages.pop(-1) # it is used to remove last character from word 
            ad = messages.insert(0,po) # it is used to add pervious removed character to first

            message2 = "".join(messages) # it is used to merge charater and convert list to string

            new_word.append(message2) # it is used to add element to new word list


    decoded_message = " ".join(new_word) # it is used to merge all word and make single string 
    print('\n', decoded_message ,'\n') 


name = input("enter your name : ")
print(f"Hello {name} welcome to Dev's chatbot with encryption : ")

while True:
    option = input('''choose what you want to do :
                   CODING (C) 
                   DECODING (D)
                   EXIT (E)
                   : ''')

    if(option == 'C' or option == 'c'):
        coding()
    elif(option == 'D' or option == 'd'):
        decoding()
    elif(option == 'E' or option == 'e'):
        exit()
    else:
        print("invalid input!!")