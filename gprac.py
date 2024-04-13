# import random
# list1 = ["apple", "banana", "orange"]
# v = random.randint(0,2)
# choice = list1[v]
# print(v)
# print(choice)

# import random
# def roll():
#     minimum_val=1
#     maximum_val=6
#     roll=random.randint(minimum_val,maximum_val)
#     return roll
# while True:
#     players=int(input("Enter players (2-4): "))
#     if 2<=players<=4:
#         break
#     else:
#         print("Range is (2-4)")
# max_score=10
# player_scores=[0]*players
# while max(player_scores)<max_score:
#     for i in range(players):
#         print(f"Player {i+1} turn has just started!")
#         print(f"Your score is: ",player_scores[i])
#         current_score=0
#         while True:
#             you_roll=input("You want to roll(yes/no): ")
#             if you_roll.lower()=='no':
#                 break
#             value=roll()
#             if value==1:
#                 print("You rolled 1! Turn done!")
#                 break
#             else:
#                 current_score+=value
#                 print("You rolled a ",value)
#             print("Your current score is: ",current_score)
#         player_scores[i]+=current_score
#         print("Your total score is: ",player_scores[i])

# max_score=max(player_scores)
# winner=player_scores.index(max_score)
# print(f"Player {winner+1} is the winner with a score of: {max_score}")

#ROCK PAPER SCISSORS
# import random
# user_wins=0
# comp_wins=0
# Ties=0
# game_options=['rock','paper','scissor']
# print("|WELCOME TO THE GAME|")
# while True:
#     option=str(input("Enter ROCK/PAPER/SCISSOR OR (quit to exit): ")).lower()
#     if option=='quit':
#         break
#     else:
#         if option not in game_options:
#             print("Plz choose [rock,paper or scissor]")
#             continue
#     comp_option=random.choice(game_options)
#     print("Computer picked: ",comp_option)
#     if option=='rock' and comp_option=='scissor':
#         print("You won!")
#         user_wins+=1
#         continue
#     elif option=='scissor' and comp_option=='paper':
#         print("You won!")
#         user_wins+=1
#         continue
#     elif option=='paper' and comp_option=='rock':
#         print("You won!")
#         user_wins+=1
#         continue
#     elif option==comp_option:
#         print("Tied")
#         Ties+=1
#         continue
#     else:
#         print("Computer won")
#         comp_wins+=1
# print("\nSummary:")
# print(f"You won {user_wins} times")
# print(f"Computer won {comp_wins} times")
# print("Your ties: ",Ties)
# print("Bye.See you next time.")


class Cars:
    def __init__(self,colour,model):   #init is the method or function which is automatically called in a class
        self.col=colour   #self. means that self is the object and the thing which comes after
                             #. means that it is the attribute of that object(specific object) for that instance
        self.mod=model
    def car(self):
        return f"{self.col} is driving and its model is {self.mod}"

car1=Cars("Red",2021)    
print(car1.car())    
car2=Cars("Black",2024)        
print(car2.car())