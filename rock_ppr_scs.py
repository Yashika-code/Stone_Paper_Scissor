import random
User=input("enter your name : ")
item_list=["Rock","Paper","Scissor"]
user_choice=input("enter your move = Rock,Paper,Scissor : ")
comp_choice=random.choice(item_list)
print(f"{User} : ",user_choice)
print("computer : ",comp_choice)
ch=str(input("Do You Want to play"))

while ch.capitalize() == "Yes":
    if user_choice.capitalize()==comp_choice.capitalize():
        print("Both tie")
    elif comp_choice.capitalize()=="Rock" and user_choice.capitalize()=="Scissor" :
        print("computer win!!")
    elif comp_choice.capitalize()=="Rock" and user_choice.capitalize()=="Paper" :
        print(f"{User} win!!")
    elif comp_choice.capitalize()=="Paper" and user_choice.capitalize()=="Rock" :
        print("computer win!!")
    elif comp_choice.capitalize()=="Paper" and user_choice.capitalize()=="Scissor" :
        print(f"{User} win!!")
    elif comp_choice.capitalize()=="Scissor" and user_choice.capitalize()=="Rock" :
        print(f"{User} win!!")
    elif comp_choice.capitalize()=="Scissor" and user_choice.capitalize()=="Paper" :
        print("computer win!!")
    ch=str(input("Do You Want to continue : "))
    