from operator import itemgetter
import random
# Function goes hwew

# checks user enters an integer more than zero
def check_rounds():
    while True:
        response = input("How many rounds would you like to play ? (for continuous mode press enter): ")
        round_error = "Please type either <enter> " \
            "or an integer that is more than 0"
        # If infinite mode not chosen, check response
        # # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

               # If response is too low, go back to
               # start of loop
                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue
        return response

# checks user enters a valid option based on a list
def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in thr list (or the first letter of an item), the
        # full item name is returned

        for item in rps_list:
            if response == item[0] or response == item:
                return item

        # output error if item is not in list
        print(error)
        print()

def instructions():
    print()
    print("***** HOW TO PLAY *****")
    print("- Rock beats scissors")
    print("- Scissors beats paper")
    print("- Paper beats rock")

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please say yes / no")

def statement_generator(statement, decoration):

    sides = decoration * 3

    sides = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main routine goes here
statement_generator("Welcome to the Rock Paper Scissors Game", "*" )
print()

played_before = yes_no ("Have you played the game before? ")

if played_before == "no":
    instructions()

print()

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before.
# If 'yes', show instructions


# ask user for # of rounds then loop...
rounds_played = 0 
rounds_lost = 0
rounds_drawn = 0
rounds_won = 0
game_summary = []
mode = "regular"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

if rounds == "":
    mode = "infinite"
    rounds = 5

end_game = "no"
while end_game == "no" and rounds_played < rounds:

    # Start of Game Play Loop
    
    # Rounds Heading
    print()

    if mode == "infinite":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
        rounds += 1
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose_instruction = "Please choose rock (r), paper (p) or scissors (s) "
    print()

    choose_error = "Please chose from rock / paper / scissors (or xxx to quit) "


    # Ask user for choice and check it's valid
    choose = choice_checker(choose_instruction, rps_list, choose_error)
    
    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print(comp_choice, end="\t")
    
    # End game if requested # of rounds has been played
    if choose == "xxx" and rounds_played > 0:
        break
    elif choose == "xxx":
        print("you need to play at least one round")
        continue
    
    # Compare options...    
    if comp_choice == choose:
        result = "tie"
        rounds_drawn += 1
    elif choose == "rock" and comp_choice == "scissors":
        result = "won"
        rounds_won += 1
    elif choose == "paper" and comp_choice == "rock":
        result = "won"
        rounds_won += 1
    elif choose == "scissors" and comp_choice == "paper":
        result = "won"
        rounds_won += 1
    else:
        result = "lost"
        rounds_lost += 1

    if result == "tie":
        feedback = "It's a tie"
    else:
        feedback = "{} vs {} - you {}".format(choose, comp_choice, result)
   
    # Output results...
    print(feedback)
    outcome = "Round {}: {}".format(rounds_played + 1, feedback)
    game_summary.append(outcome)

    rounds_played += 1
    

    if rounds_played == rounds:
        break

  

# Quick Calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# Ask user if they want to see their game history.
# If 'yes; show game history


# **** Calculate Game Stats ****
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100

print()
print("***** Game History *****")
for game in game_summary:
    print(game)

print()

# Displays game stats with % values to the nearest whole number
print("****** Game Statistics ******")
print("Win: {}, ({:.0f}%)\nLoss: {}, ({:.0f}%)\nTie: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lose, rounds_drawn, percent_tie))
# End of Game Statements
print()
print('***** End Game Summary *****')
print("Won: {} \t|\t Lost: {} \t|\t Draw: {}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thanks for playing")

