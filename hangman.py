import random
import hangmn_stges
data_house=['argentina', 'brazil', 'canada', 'denmark', 'egypt', 'france', 'germany', 
            'hungary', 'india', 'japan', 'kenya', 'luxembourg', 'mexico', 'netherlands',
            'oman', 'portugal', 'qatar', 'russia', 'spain', 'turkey', 'unitedkingdom', 
            'vietnam', 'yemen', 'zambia', 'lion', 'tiger', 'elephant', 'giraffe', 
            'zebra', 'kangaroo', 'panda', 'koala', 'leopard', 'cheetah', 'dolphin',
            'shark', 'whale', 'penguin', 'eagle', 'parrot', 'sparrow', 'peacock', 
            'swan', 'ostrich', 'flamingo', 'robin', 'hummingbird', 'kingfisher', 'owl', 
            'rose', 'tulip', 'lily', 'daisy', 'sunflower', 'orchid', 'daffodil', 'lavender', 
            'jasmine', 'marigold',  'hibiscus', 'poppy', 'lotus', 'iris',
            'bluebell', 'violet', 'camellia', 'dahlia', 'apple', 'banana', 'cherry', 'date', 
            'fig', 'grape', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince',
            'raspberry', 'strawberry', 'tangerine', 'watermelon', 'xigua', 'zucchini']

chance=7   #the total chances for guess will be seven


def generate_Random_Word():
    system_slected=random.choice(data_house)
   
    return system_slected

# The fucntion will select a radom word from the list


print("!!!Let's play hangman!!!")
print("You have only seven lives so try to guess the word within six attempts! Good luck!")
system_selected=generate_Random_Word()   # calling the function
# print(system_selected)
display_list=[]
for itmes in system_selected:
        display_list.append("_")
print(display_list)

# this loop will dispaly a list with spaces equal to the number of alphabet in the selected word

game_Over=False
while not game_Over:
    guessed_letter=input("Enter your guess: ").lower()  #ask for input with the user and 
                                                         # convert that into  lower case 
    for position in range(len(system_selected)):
        letter= system_selected[position] # get a letter of system_selected word
        if letter==guessed_letter:
            display_list[position]= guessed_letter #if the user input aplhabet matches to the system 
                                                  #selected word, then diplay list should include 
                                                  # the user input in the exact postion
    
    
    
    print(display_list)
    if guessed_letter not in system_selected:
        chance-=1
        if chance==0:
            print("OOPs!!you lose:")
            game_Over= True
            
            
    if '_' not in display_list:
        print("Congratulations!!you won:")
        game_Over= True

    print(hangmn_stges.stages[chance]) #to disply stages of hangman