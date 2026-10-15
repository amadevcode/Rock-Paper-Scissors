import random

username = input("What's your username?\n>>")
print(f"\n\nWelcome {username.title()}!\n\n")

play_id = {"r" : 1, "rock" : 1, "p" : 2, "paper" : 2, "s" : 3, "scissors" : 3, "q" : 4, "quit" : 4}
score = {"user" : 0, "bot" : 0}

while True:
    user_play = input(f"What do you want to play?\n(R-Rock, P-Paper, S-Scissors, Q-Quit)\n{username.title()}@rps.console>>")
    user_play = user_play.lower()
    user_play = play_id[user_play]
    bot_play = random.randint(1, 3)
    if (user_play == 1 and bot_play == 3) or (user_play == 3 and bot_play == 2) or (user_play == 2 and bot_play == 1):
        score["user"] += 1
        print(f"\n\n You won! You {score["user"]} - {score["bot"]} Bot\n\n")
    elif user_play == bot_play:
        print(f"\n\n Tie! You {score["user"]} - {score["bot"]} Bot\n\n")
    elif user_play == 4:
        break
    else:
        score["bot"] += 1
        print(f"\n\n The bot won! You {score["user"]} - {score["bot"]} Bot\n\n")
