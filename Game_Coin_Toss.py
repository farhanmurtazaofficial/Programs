import random
class Coin:
    def toss_coin(self):
        return random.choice(["Head","Tail"])

team = Coin()
pakistan_team = team.toss_coin()
if pakistan_team == "Head":
    decison = input("Pakitan you want to bat first y/n:")
    if decison.lower().strip() =="y":
        print("Thanks Pakistan going to Bat.")
    else:
        print("Thanks for Decision Pakistan going to Bowl.")
else:
    decison = input("India you want to bat first y/n:")
    if decison.lower().strip() =="y":
        print("Thanks India going to Bat.")
    else:
        print("Thanks for Decision India going to Bowl.")