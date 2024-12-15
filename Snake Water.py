print("Welcome to the game snake-water-gun!")
print("You have enter any one snake,water,gun")
op1=("snake,Snake,SNAKE")
op2=("water,Water,WATER")
op3=("Gun,gun,GUN")
snake=input("Choose One(snake,gun or water):")
if(snake in op1):
    print("You loose,as gun killed you")
elif(snake in op2):
    print("You drinked by snake,You loose!")
elif(snake in op3):
    print("You win as you are gun and slay snake!")
else:
    print("What are you doing! type that is in bracket(You have to choose)")
