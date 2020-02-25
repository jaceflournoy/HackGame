import random
from colorama import Fore, Back, Style

print('''Welcome to the Hacking Simulator.
-----------------''')

def menu():
    print(Style.RESET_ALL + '''Jobs:
1) Social Engineer your local McDonalds for a free lunch. (93%)
2) Obtain the Facebook password of your enemy. (86%)
3) Download a torrent warez rip of MS Windows. (79%)
4) Make a stealth Paypal account. (72%)
5) E-Whore some rich dude online for pocket cash. (65%)
6) Dox someone you hate and release it on Twitter. (58%)
7) Create an Amazon phishing page. (51%)
8) Use an account generator to login to Netflix. (44%)
9) Infect your co-worker with a virus. (37%)
10) Hack into your neighbors Wifi network. (30%)
11) SQL inject a website to dump their database. (23%)
12) Spread a Bitcoin Stealer. (16%)
13) Hack into NASA looking for proof of the moon landing. (9%)
---
0) Exit Game
''')

init_money = 500
money = init_money

def play():
    global money
    while(money>0):
        input("Press Any Key to continue...")
        menu()
        hackJob = input(str("You currently have $" + str(money) + " - Choose a job: "))
        jobs(hackJob)
        if money < 0:
            input("You do not have enough money. Game over.")

def jobs(jobChoice):
    global money
    while(True):
        chance = random.randint(1,100)
        if jobChoice == "1": # Social Engineer your local McDonalds for a free lunch.
            win = random.randint(2,5) # win amount
            if chance <= 93:
                print(Fore.GREEN + "Awesome! You got a free Big Mac and fries.")
                print(Fore.GREEN + "Cash earned: $" + str(win))
                money+=win
                return True
            elif chance > 93:
                print(Fore.RED + "You were asked to leave the store.")
                money-=random.randint(1,3)
                return True
        if jobChoice == "2": # Obtain the Facebook password of your enemy. (86%)
            win = random.randint(5,10) # win amount
            if chance <= 86:
                print(Fore.GREEN + "The password is in your possession.")
                print(Fore.GREEN + "Cash earned: $" + str(win))
                money+=win
                return True
            elif chance > 86:
                print(Fore.RED + "You were locked out of the account.")
                money-=random.randint(3,8)
                return True
        if jobChoice == "3": # Download a torrent warez rip of MS Windows. (79%)
            win = random.randint(10,20) # win amount
            if chance <= 79:
                print(Fore.GREEN + "Enjoy your free Windows OS!")
                print(Fore.GREEN + "Cash earned: $" + str(win))
                money+=win
                return True
            elif chance > 79:
                print(Fore.RED + "You wasted all day on bad downloads.")
                money-=random.randint(5,10)
                return True
        if jobChoice == "4": # Make a stealth Paypal account. (72%)
            win = random.randint(15,30) # win amount
            if chance <= 72:
                print(Fore.GREEN + "Account successfully created.")
                print(Fore.GREEN + "Cash earned: $" + str(win))
                money+=win
                return True
            elif chance > 72:
                print(Fore.RED + "Your account was banned from Paypal.")
                money-=random.randint(10,15)
                return True
        if jobChoice == "5": # E-Whore some rich dude online for pocket cash. (65%)
            win = random.randint(30,45) # win amount
            if chance <= 65:
                print(Fore.GREEN + "You got paid.")
                print(Fore.GREEN + "Cash earned: $" + str(win))
                money+=win
                return True
            elif chance > 65:
                print(Fore.RED + "You were caught and removed from the site!")
                money-=random.randint(10,15)
                return True
        if jobChoice == "6": # Dox someone you hate and release it on Twitter. (58%)
            win = random.randint(45,60) # win amount
            if chance <= 58:
                print(Fore.GREEN + "DOX was successful.")
                print(Fore.GREEN + "Cash earned: $" + str(win))
                money+=win
                return True
            elif chance > 58:
                print(Fore.RED + "They found out and are now trying to DOX you.")
                money-=random.randint(15,20)
                return True
        if jobChoice == "7": # Create an Amazon phishing page. (51%)
            win = random.randint(60,75) # win amount
            if chance <= 51:
                print(Fore.GREEN + "You're successfully harvesting credentials.")
                print(Fore.GREEN + "Cash earned: $" + str(win))
                money+=win
                return True
            elif chance > 51:
                print(Fore.RED + "You are banned from the hosting provider.")
                money-=random.randint(20,25)
                return True
        if jobChoice == "8": # Use an account generator to login to Netflix. (44%)
            win = random.randint(75,100) # win amount
            if chance <= 44:
                print(Fore.GREEN + "Success! Grab some popcorn.")
                print(Fore.GREEN + "Cash earned: $" + str(win))
                money+=win
                return True
            elif chance > 44:
                print(Fore.RED + "Fail!")
                money-=random.randint(30,35)
                return True
        if jobChoice == "9": # Infect your co-worker with a virus. (37%)
            win = random.randint(100,150) # win amount
            if chance <= 37:
                print(Fore.GREEN + "You have full system access to their machine.")
                print(Fore.GREEN + "Cash earned: $" + str(win))
                money+=win
                return True
            elif chance > 37:
                print(Fore.RED + "Your manager calls you into the office.")
                money-=random.randint(30,35)
                return True
        if jobChoice == "10": # Hack into your neighbors Wifi network. (30%)
            win = random.randint(150,250) # win amount
            if chance <= 30:
                print(Fore.GREEN + "Enjoy your free Wifi!")
                print(Fore.GREEN + "Cash earned: $" + str(win))
                money+=win
                return True
            elif chance > 30:
                print(Fore.RED + "You hear a loud knock on your door.")
                money-=random.randint(30,35)
                return True
        if jobChoice == "11": # SQL inject a website to dump their database. (23%)
            win = random.randint(250,350) # win amount
            if chance <= 23:
                print(Fore.GREEN + "You've acquired a large list of user credentials.")
                print(Fore.GREEN + "Cash earned: $" + str(win))
                money+=win
                return True
            elif chance > 23:
                print(Fore.RED + "The website noticed your activity and patched the vulnerability.")
                money-=random.randint(30,35)
                return True
        if jobChoice == "12": # Spread a Bitcoin Stealer. (16%).
            win = random.randint(500,650) # win amount
            if chance <= 16:
                print(Fore.GREEN + "You're gaining 1 BTC/day. ")
                print(Fore.GREEN + "Cash earned: $" + str(win))
                money+=win
                return True
            elif chance > 16:
                print(Fore.RED + "Your BTC Balance remains at 0.")
                money-=random.randint(50,75)
                return True
        if jobChoice == "13": # Hack into NASA looking for proof of the moon landing. (9%)
            win = random.randint(750,1000) # win amount
            if chance <= 9:
                print(Fore.GREEN + "You've discovered footage that proves the moon landing was real.")
                print(Fore.GREEN + "Cash earned: $" + str(win))
                money+=win
                return True
            elif chance > 9:
                print(Fore.RED + "There is now an FBI file with your name on it.")
                money-=random.randint(100,125)
                return True
        elif jobChoice == "0": # Exit Game
            print(Fore.GREEN + "You finished with $" + str(money))
            exit()
        else: # Error
            print("error!")

play()